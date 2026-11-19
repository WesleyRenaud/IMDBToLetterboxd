from __future__ import annotations

import re


class YearParser():
   @classmethod
   def parse( cls, raw: str ) -> str:
      if not raw:
         return ''

      match = re.search( r'(19|20)\d{2}', raw )
      return match.group( 0 ) if match else ''
