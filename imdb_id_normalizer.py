from __future__ import annotations

import re


class ImdbIdNormalizer():
   @classmethod
   def normalize( cls, raw: str, url: str = '' ) -> str:
      candidate = raw.strip()

      if not candidate and url:
         match = re.search( r'(tt\d+)', url, flags=re.IGNORECASE )

         if match:
            candidate = match.group( 1 )

      if not candidate:
         return ''

      if candidate.isdigit():
         candidate = f'tt{ candidate }'

      if not re.fullmatch( r'tt\d+', candidate, flags=re.IGNORECASE ):
         return ''

      return candidate.lower()
