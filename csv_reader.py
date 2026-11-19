from __future__ import annotations

import csv
from io import StringIO
from pathlib import Path


class CsvReader():
   ENCODINGS = ( 'utf-8-sig', 'utf-8', 'cp1252', 'latin-1' )


   @classmethod
   def open( cls, path: Path ) -> tuple[ StringIO, csv.DictReader, str ]:
      last_error: Exception | None = None

      for encoding in cls.ENCODINGS:
         try:
            # Decode the full file up front so a late bad byte doesn't fail mid-convert.
            text = path.read_text( encoding=encoding )

            if '\x00' in text:
               continue

            handle = StringIO( text )
            reader = csv.DictReader( handle )

            if not reader.fieldnames:
               raise ValueError( f'{ path.name } has no header row.' )

            return handle, reader, encoding
         except UnicodeDecodeError as exc:
            last_error = exc
            continue

      raise ValueError(
         f'Could not decode { path } with tried encodings { cls.ENCODINGS }: { last_error }'
      )
