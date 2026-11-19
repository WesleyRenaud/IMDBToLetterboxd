from __future__ import annotations

import argparse


class ConvertArgsParser():
   @classmethod
   def parse( cls ) -> argparse.Namespace:
      parser = argparse.ArgumentParser(
         description='Convert IMDb ratings CSV exports to Letterboxd import CSV.'
      )
      parser.add_argument(
         'input',
         nargs='?',
         help='Path to an IMDb ratings CSV. Defaults to the newest *.csv in input/.',
      )
      parser.add_argument(
         '-o',
         '--output',
         help='Output CSV path. Defaults to output/letterboxd_YYYYMMDD_HHMMSS.csv',
      )
      parser.add_argument(
         '--include-tv',
         action='store_true',
         help='Also include TV series / mini-series / episodes.',
      )
      parser.add_argument(
         '--include-all',
         action='store_true',
         help='Include every title type present in the IMDb export.',
      )
      return parser.parse_args()
