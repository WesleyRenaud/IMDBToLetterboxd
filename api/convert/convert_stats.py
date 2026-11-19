from __future__ import annotations

from dataclasses import dataclass, field

from .skip_reason_total import SkipReasonTotal


@dataclass
class ConvertStats():
   rows_in: int = 0
   rows_out: int = 0
   skipped: int = 0
   encoding: str = ''
   skip_reasons: list[ SkipReasonTotal ] = field( default_factory=list )


   def record_skip( self, reason: str ) -> None:
      label = reason or 'unknown'
      self.skipped += 1

      for index, total in enumerate( self.skip_reasons ):
         if total.reason == label:
            self.skip_reasons[ index ] = SkipReasonTotal( label, total.count + 1 )
            return

      self.skip_reasons.append( SkipReasonTotal( label, 1 ) )


   def ordered_skip_reasons( self ) -> list[ SkipReasonTotal ]:
      return sorted(
         self.skip_reasons,
         key=lambda total: ( -total.count, total.reason ),
      )
