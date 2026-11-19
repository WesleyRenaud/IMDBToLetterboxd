from __future__ import annotations

import re
from datetime import datetime


class WatchedDateParser():
   @classmethod
   def parse( cls, raw: str ) -> str:
      if not raw:
         return ''

      text = raw.strip()

      # Already YYYY-MM-DD (optionally with time)
      if re.match( r'^\d{4}-\d{2}-\d{2}', text ):
         return text[ :10 ]

      for fmt in ( '%Y/%m/%d', '%m/%d/%Y', '%d/%m/%Y', '%Y-%m-%d %H:%M:%S' ):
         try:
            return datetime.strptime( text, fmt ).strftime( '%Y-%m-%d' )
         except ValueError:
            continue

      match = re.search( r'(\d{4}-\d{2}-\d{2})', text )
      return match.group( 1 ) if match else ''
