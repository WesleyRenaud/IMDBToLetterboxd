# IMDb → Letterboxd ratings converter

Convert an IMDb ratings export CSV into Letterboxd’s import CSV format (stdlib Python only).

## Layout

```text
convert.py                 # thin CLI entrypoint
*.py                       # one class per file at repo root (TorontoZooGuide-style)
input/                     # drop IMDb ratings CSVs here
output/                    # Letterboxd import CSVs land here
```

There is no nested package folder named like the project; modules live flat at the repo root.

## 1. Export from IMDb

1. Sign in at [imdb.com](https://www.imdb.com) (website, not the app).
2. Open **Your Ratings** from your account menu.
3. Click **Export**.
4. Download the CSV when it’s ready (IMDb may send you to an exports page).

The file typically includes columns like `Const`, `Your Rating`, `Date Rated`, `Title`, `Title Type`, `Year`, and `Directors`.

## 2. Put the file here

Copy the downloaded CSV into:

```text
input/
```

Example: `input/ratings.csv`

## 3. Run the converter

From this folder:

```bash
python3 convert.py
```

That uses the newest `*.csv` in `input/` and writes a Letterboxd-ready file to `output/`.

Useful options:

```bash
# Explicit input / output paths
python3 convert.py input/ratings.csv -o output/letterboxd.csv

# Include TV series / episodes (skipped by default)
python3 convert.py --include-tv

# Keep every IMDb title type
python3 convert.py --include-all
```

### What it does

- Maps IMDb ratings **1–10** → Letterboxd **0.5–5** (divide by 2)
- Writes Letterboxd columns: `imdbID`, `Title`, `Year`, `Directors`, `Rating`, `WatchedDate`
- Uses `imdbID` (`tt…`) when present so Letterboxd can match titles exactly
- Skips empty/invalid ratings and, by default, non-film title types
- Leaves missing years blank (matching still works via IMDb ID)
- Reads common encodings (`utf-8`, `cp1252`, etc.) and writes UTF-8

## 4. Import into Letterboxd

1. Open Letterboxd on a desktop browser.
2. Go to **Settings → Import** (or [letterboxd.com/import](https://letterboxd.com/import/)).
3. Upload the CSV from `output/`.
4. Review matches. Optionally create diary entries from `WatchedDate` if those dates are real watch dates (IMDb’s “Date Rated” is when you rated the title, which may not be the day you watched it).
5. Confirm the import carefully — there is no undo.

Letterboxd’s import format docs: [letterboxd.com/about/importing-data](https://letterboxd.com/about/importing-data/)

## Notes

- No scraping and no account credentials are required.
- Letterboxd can also import some IMDb export files directly; this script produces their generic Letterboxd CSV format with half-star ratings.
- Python modules at the repo root follow one class per file, with the class name matching the file stem.
