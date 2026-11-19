from __future__ import annotations

from dataclasses import dataclass


@dataclass( frozen=True )
class FieldMap():
   imdb_id: str = ''
   rating: str = ''
   date_rated: str = ''
   title: str = ''
   year: str = ''
   directors: str = ''
   title_type: str = ''
   url: str = ''


   def missing_required( self ) -> list[ str ]:
      missing: list[ str ] = []

      if not self.title:
         missing.append( 'title' )

      if not self.rating:
         missing.append( 'rating' )

      return missing
