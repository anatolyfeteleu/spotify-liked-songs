from os import getenv
from pathlib import Path


# Configuration settings
# --------------------------------------------------------------------------------------------------

TIMESTAMP_FORMAT = '%d/%m'

# Base configuration
# --------------------------------------------------------------------------------------------------

LOGS_ENABLED = True
PLAYLIST_PREFIX = 'Import {}'  # note: by default - "Import %d/%m"

# Spotify configuration
# --------------------------------------------------------------------------------------------------

CLIENT_ID = getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URL = getenv('SPOTIFY_REDIRECT_URL')  # NOQA
SCOPES = [
    'user-library-read',
    'playlist-modify-private',
    'playlist-modify-public'
]
