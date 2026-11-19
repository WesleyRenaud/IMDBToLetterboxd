#!/usr/bin/env python3
"""Thin entrypoint for the IMDb → Letterboxd converter."""

from __future__ import annotations

from api.convert.convert_runner import ConvertRunner


if __name__ == '__main__':
   raise SystemExit( ConvertRunner.run() )
