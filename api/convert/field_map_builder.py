from __future__ import annotations

import re

from .field_map import FieldMap


class FieldMapBuilder():
   ALIASES = {
      'const': 'imdb_id',
      'imdbid': 'imdb_id',
      'yourrating': 'rating',
      'yourated': 'rating',
      'rating': 'rating',
      'daterated': 'date_rated',
      'created': 'date_rated',
      'title': 'title',
      'year': 'year',
      'directors': 'directors',
      'titletype': 'title_type',
      'url': 'url',
   }


   @classmethod
   def normalize_header( cls, name: str | None ) -> str:
      if name is None:
         return ''

      return re.sub( r'[^a-z0-9]+', '', name.strip().lower() )


   @classmethod
   def build( cls, fieldnames: list[ str ] ) -> FieldMap:
      headers: dict[ str, str ] = {}

      for original in fieldnames:
         key = cls.ALIASES.get( cls.normalize_header( original ) )

         if key and key not in headers:
            headers[ key ] = original

      return FieldMap(
         imdb_id=headers.get( 'imdb_id', '' ),
         rating=headers.get( 'rating', '' ),
         date_rated=headers.get( 'date_rated', '' ),
         title=headers.get( 'title', '' ),
         year=headers.get( 'year', '' ),
         directors=headers.get( 'directors', '' ),
         title_type=headers.get( 'title_type', '' ),
         url=headers.get( 'url', '' ),
      )
