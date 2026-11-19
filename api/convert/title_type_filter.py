from __future__ import annotations

import re


class TitleTypeFilter():
   # Letterboxd is film-focused; returning TV series/episodes are not supported.
   ALLOWED_TITLE_TYPES = {
      'movie',
      'short',
      'tvmovie',
      'tv special',
      'tvspecial',
      'video',
   }


   @classmethod
   def allows( cls, title_type: str ) -> bool:
      if not title_type:
         return True

      normalized = re.sub( r'\s+', ' ', title_type.strip().lower() )
      compact = normalized.replace( ' ', '' )
      allowed = { item.replace( ' ', '' ) for item in cls.ALLOWED_TITLE_TYPES }
      return compact in allowed
