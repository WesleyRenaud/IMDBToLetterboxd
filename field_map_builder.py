from __future__ import annotations

import re


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
   def build( cls, fieldnames: list[ str ] ) -> dict[ str, str ]:
      mapping: dict[ str, str ] = {}

      for original in fieldnames:
         key = cls.ALIASES.get( cls.normalize_header( original ) )

         if key and key not in mapping:
            mapping[ key ] = original

      return mapping


   @classmethod
   def get_value(
      cls,
      row: dict[ str, str | None ],
      field_map: dict[ str, str ],
      key: str,
   ) -> str:
      original = field_map.get( key )

      if not original:
         return ''

      value = row.get( original )
      return ( value or '' ).strip()
