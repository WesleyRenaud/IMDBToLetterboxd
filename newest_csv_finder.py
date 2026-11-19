from __future__ import annotations

from pathlib import Path


class NewestCsvFinder():
   @classmethod
   def find( cls, directory: Path ) -> Path:
      files = sorted(
         directory.glob( '*.csv' ),
         key=lambda path: path.stat().st_mtime,
         reverse=True,
      )

      if not files:
         raise FileNotFoundError(
            f'No CSV files found in { directory }. '
            'Export ratings from IMDb and place the file there.'
         )

      return files[ 0 ]
