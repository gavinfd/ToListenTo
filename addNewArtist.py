from gmusicapi import Mobileclient
from pprint import pprint
api = Mobileclient()

api.login('', '', Mobileclient.FROM_MAC_ADDRESS)

playlist_name = 'ToListenTo'
answer=api.search_all_access('', max_results=1)

sweet_track_ids = []
artist_id=answer['artist_hits'][0]['artist']['artistId']
response = api.get_artist_info(artist_id, include_albums=False, max_top_tracks=3, max_rel_artist=0)
for song in response['topTracks']:
    sweet_track_ids.append(song['nid'])
    playlists = api.get_all_playlists()
playlist_id = None
for playlist in playlists:
    if playlist_name in playlist['name']:
        playlist_id = playlist['id']
    if not playlist_id:
        playlist_id = api.create_playlist(playlist_name)
api.add_songs_to_playlist(playlist_id, sweet_track_ids)
