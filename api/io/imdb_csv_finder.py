from __future__ import annotations

from pathlib import Path


class ImdbCsvFinder():
   SUFFIX = '_imdb.csv'


   @classmethod
   def find_all( cls, directory: Path ) -> list[ Path ]:
      files = sorted(
         path
         for path in directory.iterdir()
         if path.is_file() and path.name.endswith( cls.SUFFIX )
      )

      if not files:
         raise FileNotFoundError(
            f'No *{ cls.SUFFIX } files found in { directory }. '
            f'Rename your IMDb export to name{ cls.SUFFIX } and place it there.'
         )

      return files


   @classmethod
   def letterboxd_output_path( cls, input_path: Path, output_dir: Path ) -> Path:
      name = input_path.name

      if not name.endswith( cls.SUFFIX ):
         raise ValueError(
            f'Input file must end with { cls.SUFFIX }: { input_path.name }'
         )

      stem = name[ : -len( cls.SUFFIX ) ]

      if not stem:
         raise ValueError(
            f'Input file needs a name before { cls.SUFFIX }: { input_path.name }'
         )

      return output_dir / f'{ stem }_letterboxd.csv'
