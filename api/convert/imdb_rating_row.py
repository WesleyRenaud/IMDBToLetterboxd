from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .field_map import FieldMap


@dataclass( frozen=True )
class ImdbRatingRow():
   title: str
   rating: str
   title_type: str
   imdb_id: str
   url: str
   year: str
   directors: str
   date_rated: str


   @classmethod
   def from_csv_row( cls, raw: Mapping[ str, str | None ], field_map: FieldMap ) -> ImdbRatingRow:
      return cls(
         title=cls._value( raw, field_map.title ),
         rating=cls._value( raw, field_map.rating ),
         title_type=cls._value( raw, field_map.title_type ),
         imdb_id=cls._value( raw, field_map.imdb_id ),
         url=cls._value( raw, field_map.url ),
         year=cls._value( raw, field_map.year ),
         directors=cls._value( raw, field_map.directors ),
         date_rated=cls._value( raw, field_map.date_rated ),
      )


   @classmethod
   def _value( cls, raw: Mapping[ str, str | None ], header: str ) -> str:
      if not header:
         return ''

      value = raw.get( header )
      return ( value or '' ).strip()
