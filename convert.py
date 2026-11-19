#!/usr/bin/env python3
"""Thin entrypoint for the IMDb → Letterboxd converter package."""

from __future__ import annotations

from imdb_to_letterboxd.convert_runner import ConvertRunner


if __name__ == '__main__':
   raise SystemExit( ConvertRunner.run() )
