from __future__ import annotations

import re


class TitleTypeFilter():
   DEFAULT_TITLE_TYPES = {
      'movie',
      'short',
      'tvmovie',
      'tv special',
      'tvspecial',
      'video',
   }
   TV_TITLE_TYPES = {
      'tvseries',
      'tv series',
      'tvminiseries',
      'tv mini series',
      'tvmini series',
      'tvepisode',
      'tv episode',
   }


   @classmethod
   def allows( cls, title_type: str, include_tv: bool, include_all: bool ) -> bool:
      if include_all or not title_type:
         return True

      normalized = re.sub( r'\s+', ' ', title_type.strip().lower() )
      compact = normalized.replace( ' ', '' )

      if compact in { item.replace( ' ', '' ) for item in cls.DEFAULT_TITLE_TYPES }:
         return True

      if include_tv and (
         compact in { item.replace( ' ', '' ) for item in cls.TV_TITLE_TYPES }
         or compact.startswith( 'tv' )
      ):
         return True

      return False
