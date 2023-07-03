import requests
import pandas as pd

from services.access_token import *
from services.spotify_playlists import *
from services.playlist_records import *
from services.track_records import *
from services.playlist_track_id_records import *
from services.track_artist_id_records import *
from services.artists_records import *

#get access token, enter client_id and client secret below
access_token = get_app_access_token('Enter client_id', "Enter client secret")

#get 10 playlist using the access token in the latin catergory. These playlists are used for consequent tasks. 
category=get_spotify_playlists("latin",10,access_token)

# get the playlist record for the 
playlist_record=get_playlist_records(access_token,category)

# get the playlist IDs and the playlist followers
track_record=get_track_records(access_token,category)

# get the playlist and track id and also the added time
playlist_track_id_records=get_playlist_track_id_records(access_token,category)

# get the artist id and track id
track_artist_id_records=get_track_artist_id_records(access_token,category)

# get the artist id and artist name
artists_record= get_artists_records(access_token,category)

#write all generated dataframes to csv.gz files
category.to_csv("csv/category_playlists_records.csv.gz", index=False)
playlist_record.to_csv("csv/playlist_record.csv.gz",index=False)
track_record.to_csv("csv/track_record.csv.gz", index=False)
playlist_track_id_records.to_csv("csv/playlist_track_id_records.csv.gz", index=False)
track_artist_id_records.to_csv("csv/track_artist_id_records.csv.gz", index=False)
artists_record.to_csv("csv/artists_records.csv.gz", index=False)









