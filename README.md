# IMDb → Letterboxd ratings converter

Convert IMDb ratings export CSVs into Letterboxd’s import CSV format.

## 1. Export from IMDb

1. Sign in at [imdb.com](https://www.imdb.com) (website, not the app).
2. Open **Your Ratings** from your account menu.
3. Click **Export**.
4. Download the CSV when it’s ready (IMDb may send you to an exports page).

## 2. Put the file here

Copy each IMDb export into `input/` and name it with a strict `_imdb.csv` suffix:

```text
input/[name]_imdb.csv
```

Example: `input/ratings_imdb.csv`

Other files in `input/` are ignored.

## 3. Run the converter

From this folder:

```bash
python3 convert.py
```

Every matching `input/[name]_imdb.csv` is converted to:

```text
output/[name]_letterboxd.csv
```

Example: `input/ratings_imdb.csv` → `output/ratings_letterboxd.csv`

IMDb ratings **1–10** become Letterboxd **0.5–5**. TV series and episodes are always skipped (Letterboxd does not support them); film-like types such as movies, shorts, TV movies, and videos are kept.

## 4. Import into Letterboxd

1. Open Letterboxd on a desktop browser.
2. Go to **Settings → Import** (or [letterboxd.com/import](https://letterboxd.com/import/)).
3. Upload the CSV from `output/` (for example `output/ratings_letterboxd.csv`).
4. Review matches. Optionally create diary entries from `WatchedDate` if those dates are real watch dates (IMDb’s “Date Rated” is when you rated the title, which may not be the day you watched it).
5. Confirm the import carefully — there is no undo.

Letterboxd’s import format docs: [letterboxd.com/about/importing-data](https://letterboxd.com/about/importing-data/)
