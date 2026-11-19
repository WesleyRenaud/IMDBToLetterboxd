from __future__ import annotations

import sys
from pathlib import Path

from .convert_stats import ConvertStats
from .converter import Converter
from ..io.imdb_csv_finder import ImdbCsvFinder
from ..paths import Paths


class ConvertRunner():
   @classmethod
   def print_stats(
      cls,
      input_path: Path,
      output_path: Path,
      stats: ConvertStats,
   ) -> None:
      print( f'Input:   { input_path }' )
      print( f'Output:  { output_path }' )
      print( f'Encoding:{ stats.encoding }' )
      print( f'Rows in: { stats.rows_in }' )
      print( f'Rows out:{ stats.rows_out }' )
      print( f'Skipped: { stats.skipped }' )

      for total in stats.ordered_skip_reasons():
         print( f'  - { total.reason }: { total.count }' )


   @classmethod
   def run( cls ) -> int:
      Paths.INPUT_DIR.mkdir( parents=True, exist_ok=True )
      Paths.OUTPUT_DIR.mkdir( parents=True, exist_ok=True )

      try:
         input_paths = ImdbCsvFinder.find_all( Paths.INPUT_DIR )
      except FileNotFoundError as exc:
         print( f'Error: { exc }', file=sys.stderr )
         return 1

      failures = 0

      for input_path in input_paths:
         output_path = ImdbCsvFinder.letterboxd_output_path(
            input_path,
            Paths.OUTPUT_DIR,
         )

         try:
            stats = Converter.convert( input_path, output_path )
         except ( FileNotFoundError, ValueError, UnicodeDecodeError, OSError ) as exc:
            print( f'Error converting { input_path.name }: { exc }', file=sys.stderr )
            failures += 1
            continue

         cls.print_stats( input_path, output_path, stats )

         if input_path is not input_paths[ -1 ]:
            print()

      return 1 if failures else 0
