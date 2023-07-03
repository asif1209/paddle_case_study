import requests, pandas as pd

def get_track_artist_id_records(access_token,category):
    
    # Get access token
   
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
            track_data=[(item["track"]["id"],item["track"]['artists'][0]["id"]) for item in playlists_data["tracks"]['items']]
            df=pd.DataFrame(track_data)
            tracks=pd.concat([tracks,df])
           
            
        else:
            print("Error:", response.status_code)
    tracks.columns=["track_id","artist_id"]
    return tracks