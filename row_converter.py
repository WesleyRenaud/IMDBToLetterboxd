from __future__ import annotations

from field_map_builder import FieldMapBuilder
from imdb_id_normalizer import ImdbIdNormalizer
from rating_parser import RatingParser
from title_type_filter import TitleTypeFilter
from watched_date_parser import WatchedDateParser
from year_parser import YearParser


class RowConverter():
   @classmethod
   def convert(
      cls,
      row: dict[ str, str | None ],
      field_map: dict[ str, str ],
      *,
      include_tv: bool,
      include_all: bool,
   ) -> tuple[ dict[ str, str ] | None, str | None ]:
      title = FieldMapBuilder.get_value( row, field_map, 'title' )

      if not title:
         return None, 'missing title'

      title_type = FieldMapBuilder.get_value( row, field_map, 'title_type' )

      if not TitleTypeFilter.allows( title_type, include_tv, include_all ):
         label = title_type or 'unknown type'
         return None, f'skipped title type ({ label })'

      rating = RatingParser.parse( FieldMapBuilder.get_value( row, field_map, 'rating' ) )

      if rating is None:
         return None, 'missing or invalid rating'

      imdb_id = ImdbIdNormalizer.normalize(
         FieldMapBuilder.get_value( row, field_map, 'imdb_id' ),
         FieldMapBuilder.get_value( row, field_map, 'url' ),
      )

      return (
         {
            'imdbID': imdb_id,
            'Title': title,
            'Year': YearParser.parse( FieldMapBuilder.get_value( row, field_map, 'year' ) ),
            'Directors': FieldMapBuilder.get_value( row, field_map, 'directors' ),
            'Rating': format( rating, 'g' ),
            'WatchedDate': WatchedDateParser.parse(
               FieldMapBuilder.get_value( row, field_map, 'date_rated' )
            ),
         },
         None,
      )
