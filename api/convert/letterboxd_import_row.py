from __future__ import annotations

from dataclasses import dataclass


@dataclass( frozen=True )
class LetterboxdImportRow():
   CSV_HEADER = (
      'imdbID',
      'Title',
      'Year',
      'Directors',
      'Rating',
      'WatchedDate',
   )

   imdb_id: str
   title: str
   year: str
   directors: str
   rating: str
   watched_date: str


   def csv_values( self ) -> tuple[ str, ... ]:
      return (
         self.imdb_id,
         self.title,
         self.year,
         self.directors,
         self.rating,
         self.watched_date,
      )
