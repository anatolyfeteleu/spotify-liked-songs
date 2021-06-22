from os import getenv

from dotenv import load_dotenv

# Setting up environment variables
# --------------------------------------------------------------------------------------------------
load_dotenv(dotenv_path='settings/variables.ini')

settings = getenv('SETTINGS', '').lower()

if settings == 'local':
    from .local import *
else:
    from .base import *
