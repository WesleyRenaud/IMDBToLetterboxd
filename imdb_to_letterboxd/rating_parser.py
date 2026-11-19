from __future__ import annotations


class RatingParser():
   @classmethod
   def parse( cls, raw: str ) -> float | None:
      if not raw:
         return None

      try:
         value = float( raw.replace( ',', '.' ) )
      except ValueError:
         return None

      if value < 1 or value > 10:
         return None

      # IMDb ratings are whole numbers; keep Letterboxd half-star increments.
      letterboxd = value / 2.0
      return round( letterboxd * 2 ) / 2
