from __future__ import annotations

import csv
from pathlib import Path

from .convert_stats import ConvertStats
from .field_map_builder import FieldMapBuilder
from .imdb_rating_row import ImdbRatingRow
from .letterboxd_import_row import LetterboxdImportRow
from .row_converter import RowConverter
from ..io.csv_reader import CsvReader
from ..paths import Paths


class Converter():
   @classmethod
   def convert( cls, input_path: Path, output_path: Path ) -> ConvertStats:
      handle, reader, encoding = CsvReader.open( input_path )
      assert reader.fieldnames is not None
      field_map = FieldMapBuilder.build( list( reader.fieldnames ) )
      missing = field_map.missing_required()

      if missing:
         handle.close()
         raise ValueError(
            f'{ input_path.name } is missing expected IMDb columns for: '
            f'{ ", ".join( missing ) }. Found: { ", ".join( reader.fieldnames ) }'
         )

      stats = ConvertStats( encoding=encoding )
      Paths.OUTPUT_DIR.mkdir( parents=True, exist_ok=True )

      with handle, output_path.open( 'w', encoding='utf-8', newline='' ) as out_handle:
         writer = csv.writer( out_handle )
         writer.writerow( LetterboxdImportRow.CSV_HEADER )

         for raw in reader:
            stats.rows_in += 1
            result = RowConverter.convert( ImdbRatingRow.from_csv_row( raw, field_map ) )

            if result.row is None:
               stats.record_skip( result.skip_reason or 'unknown' )
               continue

            writer.writerow( result.row.csv_values() )
            stats.rows_out += 1

      return stats
