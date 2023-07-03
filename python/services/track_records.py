import requests
import pandas as pd

def get_track_records(access_token,category):
    """get the information of every track in a playlist"""

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
            track_data=[(item["track"]["id"],item["track"]["name"],item["track"]["popularity"],item["track"]["uri"]) for item in playlists_data["tracks"]['items']]
            df=pd.DataFrame(track_data)
            df['playlist_id']=playlist_id
            tracks=pd.concat([tracks,df])
            
        else:
            print("Error:", response.status_code)
    tracks.columns=["track_id","name","popularity","uri","playlist_id"]
    return tracks