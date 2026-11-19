from __future__ import annotations

import csv
from pathlib import Path

from csv_reader import CsvReader
from field_map_builder import FieldMapBuilder
from letterboxd_fields import LetterboxdFields
from paths import Paths
from row_converter import RowConverter


class Converter():
   @classmethod
   def convert(
      cls,
      input_path: Path,
      output_path: Path,
      *,
      include_tv: bool = False,
      include_all: bool = False,
   ) -> dict[ str, object ]:
      handle, reader, encoding = CsvReader.open( input_path )
      assert reader.fieldnames is not None
      field_map = FieldMapBuilder.build( list( reader.fieldnames ) )

      required = { 'title', 'rating' }
      missing = sorted( required - set( field_map ) )

      if missing:
         handle.close()
         raise ValueError(
            f'{ input_path.name } is missing expected IMDb columns for: '
            f'{ ", ".join( missing ) }. Found: { ", ".join( reader.fieldnames ) }'
         )

      rows_in = 0
      rows_out = 0
      skipped = 0
      skip_reasons: dict[ str, int ] = {}

      Paths.OUTPUT_DIR.mkdir( parents=True, exist_ok=True )

      with handle, output_path.open( 'w', encoding='utf-8', newline='' ) as out_handle:
         writer = csv.DictWriter( out_handle, fieldnames=LetterboxdFields.NAMES )
         writer.writeheader()

         for row in reader:
            rows_in += 1
            converted, reason = RowConverter.convert(
               row,
               field_map,
               include_tv=include_tv,
               include_all=include_all,
            )

            if converted is None:
               skipped += 1
               skip_reasons[ reason or 'unknown' ] = (
                  skip_reasons.get( reason or 'unknown', 0 ) + 1
               )
               continue

            writer.writerow( converted )
            rows_out += 1

      return {
         'rows_in': rows_in,
         'rows_out': rows_out,
         'skipped': skipped,
         'encoding': encoding,
         'skip_reasons': skip_reasons,
      }
