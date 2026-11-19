from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from .convert_args_parser import ConvertArgsParser
from .converter import Converter
from .newest_csv_finder import NewestCsvFinder
from .paths import Paths


class ConvertRunner():
   @classmethod
   def default_output_path( cls ) -> Path:
      stamp = datetime.now().strftime( '%Y%m%d_%H%M%S' )
      return Paths.OUTPUT_DIR / f'letterboxd_{ stamp }.csv'


   @classmethod
   def run( cls ) -> int:
      args = ConvertArgsParser.parse()
      Paths.INPUT_DIR.mkdir( parents=True, exist_ok=True )
      Paths.OUTPUT_DIR.mkdir( parents=True, exist_ok=True )

      try:
         input_path = (
            Path( args.input ).expanduser()
            if args.input
            else NewestCsvFinder.find( Paths.INPUT_DIR )
         )

         if not input_path.is_file():
            raise FileNotFoundError( f'Input file not found: { input_path }' )

         output_path = (
            Path( args.output ).expanduser()
            if args.output
            else cls.default_output_path()
         )
         stats = Converter.convert(
            input_path,
            output_path,
            include_tv=args.include_tv,
            include_all=args.include_all,
         )
      except ( FileNotFoundError, ValueError, UnicodeDecodeError, OSError ) as exc:
         print( f'Error: { exc }', file=sys.stderr )
         return 1

      print( f'Input:   { input_path }' )
      print( f'Output:  { output_path }' )
      print( f'Encoding:{ stats[ "encoding" ] }' )
      print( f'Rows in: { stats[ "rows_in" ] }' )
      print( f'Rows out:{ stats[ "rows_out" ] }' )
      print( f'Skipped: { stats[ "skipped" ] }' )
      reasons = stats.get( 'skip_reasons' ) or {}

      if reasons:
         for reason, count in sorted(
            reasons.items(),
            key=lambda item: ( -item[ 1 ], item[ 0 ] ),
         ):
            print( f'  - { reason }: { count }' )

      return 0
