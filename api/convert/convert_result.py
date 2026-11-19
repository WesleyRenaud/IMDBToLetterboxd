from __future__ import annotations

from dataclasses import dataclass

from .letterboxd_import_row import LetterboxdImportRow


@dataclass( frozen=True )
class ConvertResult():
   row: LetterboxdImportRow | None = None
   skip_reason: str | None = None


   @classmethod
   def kept( cls, row: LetterboxdImportRow ) -> ConvertResult:
      return cls( row=row )


   @classmethod
   def skipped( cls, reason: str ) -> ConvertResult:
      return cls( skip_reason=reason )
