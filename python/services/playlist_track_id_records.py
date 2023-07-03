import requests,pandas as pd


def get_playlist_track_id_records(access_token,category):
    
    # Get the added time for each track in the playlist
 
    headers = {
            "Authorization": f"Bearer {access_token}" 
        }
    
    playlist_records= pd.DataFrame(category["id"])
    tracks=pd.DataFrame()
    
    for playlist_id in playlist_records["id"]:
       
        base_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        response = requests.get(base_url, headers=headers)
        
        if response.status_code == 200:
            playlists_data = response.json()
            track_data=[(item["track"]["id"],item["added_at"]) for item in playlists_data["tracks"]['items']]
            df=pd.DataFrame(track_data)
            df['playlist_id']=playlist_id
            tracks=pd.concat([tracks,df])
            
        else:
            print("Error:", response.status_code)
    tracks.columns=["track_id","added_at","playlist_id"]
    return tracks