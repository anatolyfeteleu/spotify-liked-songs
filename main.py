import sys
from datetime import datetime
from typing import Dict, Iterable

import spotipy
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyOAuth

from extensions import Beautify
from settings import base as settings


class SpotifyClient:

    # note: {self.ITEMS_PER_REQUEST} items per request, limitation Spotify API
    ITEMS_PER_REQUEST = 100

    def __init__(self):

        self.client = self.get_client()

    @staticmethod
    @Beautify
    def get_client() -> spotipy.Spotify:
        """
        Created an instance of Spotify client
        :return: spotipy.Spotify
        """

        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope=settings.SCOPES,
                client_id=settings.CLIENT_ID,
                client_secret=settings.CLIENT_SECRET,
                redirect_uri=settings.REDIRECT_URL,
            ),
        )

    @staticmethod
    @Beautify
    def generate_playlist_name() -> str:
        """
        Generates playlist name
        :return: Str
        """

        now_f = datetime.now().strftime(settings.TIMESTAMP_FORMAT)
        return settings.PLAYLIST_PREFIX.format(now_f)

    @Beautify
    def get_user(self) -> Dict:
        """
        Returns details of current user
        :return: Dict
        """

        return self.client.me()

    @Beautify
    def get_user_id(self) -> str:
        """
        Returns user identifier
        :return: Str
        """

        user = self.get_user()
        assert user, 'User data is required'

        return user.get('id')

    @Beautify
    def create_playlist(self) -> Dict:
        """
        Creates a playlist, that contains tracks from section "Liked tracks".
        :return: Dict
        """

        return self.client.user_playlist_create(
            name=self.generate_playlist_name(),
            user=self.get_user_id()
        )

    @Beautify
    def put_track_ids_to_playlist(self, playlist_id: str, track_ids: Iterable):
        """
        Puts tracks by identifiers into playlist by playlist id.
        :param playlist_id: str
        :param track_ids: set
        :return: None object
        """

        self.client.playlist_add_items(playlist_id=playlist_id, items=track_ids)

    @Beautify
    def resave_liked_tracks(self, playlist_id: str) -> None:
        """
        Iterates over 'Liked tracks' and puts every track into playlist by playlist id
        :param playlist_id: str
        :return: None object
        """

        results = self.client.current_user_saved_tracks(limit=50)
        track_ids = list()

        while results.get('next') or results['items']:
            for idx, item in enumerate(results['items']):
                track_ids.append(item['track']['id'])

            if len(track_ids) == self.ITEMS_PER_REQUEST:
                self.put_track_ids_to_playlist(playlist_id=playlist_id, track_ids=track_ids)
                track_ids = list()

            if not results.get('next'):
                break

            # flip page forward
            results = self.client.next(results)

        self.put_track_ids_to_playlist(playlist_id=playlist_id, track_ids=track_ids)


if __name__ == '__main__':

    try:
        client = SpotifyClient()
        playlist = client.create_playlist()
        client.resave_liked_tracks(playlist_id=playlist.get('id'))
    except SpotifyException as exc:
        sys.stdout.write(
            'DETAIL: Something went wrong\n'
            f'EXCEPTION: {exc}'
        )
    except AssertionError as exc:
        sys.stdout.write(
            'DETAIL: Internal error, check source code\n'
            f'EXCEPTION: {exc}'
        )
    else:
        sys.stdout.write('COMPLETED')
