from __future__ import annotations

from .convert_result import ConvertResult
from .imdb_rating_row import ImdbRatingRow
from .letterboxd_import_row import LetterboxdImportRow
from .title_type_filter import TitleTypeFilter
from ..parsers.imdb_id_normalizer import ImdbIdNormalizer
from ..parsers.rating_parser import RatingParser
from ..parsers.watched_date_parser import WatchedDateParser
from ..parsers.year_parser import YearParser


class RowConverter():
   @classmethod
   def convert( cls, row: ImdbRatingRow ) -> ConvertResult:
      if not row.title:
         return ConvertResult.skipped( 'missing title' )

      if not TitleTypeFilter.allows( row.title_type ):
         label = row.title_type or 'unknown type'
         return ConvertResult.skipped( f'skipped title type ({ label })' )

      rating = RatingParser.parse( row.rating )

      if rating is None:
         return ConvertResult.skipped( 'missing or invalid rating' )

      return ConvertResult.kept(
         LetterboxdImportRow(
            imdb_id=ImdbIdNormalizer.normalize( row.imdb_id, row.url ),
            title=row.title,
            year=YearParser.parse( row.year ),
            directors=row.directors,
            rating=format( rating, 'g' ),
            watched_date=WatchedDateParser.parse( row.date_rated ),
         )
      )
