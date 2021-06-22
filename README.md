# Spotify 'Liked songs' migration tool.

Based on [Python](https://www.python.org/) (3.9.5) and [Spotipy](https://spotipy.readthedocs.io/) (2.18.0).

## Description
Used to transfer your tracks from `Liked songs` to a playlist for further action.  
Was written to export all tracks from `Liked songs` to Apple Music `Liked songs`.

## Summary
`settings/` - directory in which the tool settings and variables are stored.

## How to:
1. Create and use python virtual environment (VE)  
   1.1 Run command `python3 -m venv <VE name>` to create VE  
   1.2 Run command `source <VE name>/bin/activate`
2. Fill variables in `settings/variables.ini`
4. (Optional) Modified tool configuration (`settings/base.py`)
5. Run migration tool - `python3 main.py`