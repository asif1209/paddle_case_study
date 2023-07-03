import requests,pandas as pd



def get_playlist_records(access_token,category):
    """Contains the playlist IDs and the playlist followers from the previously acquired """
   
    headers = {
            "Authorization": f"Bearer {access_token}" 
        }
    
    playlist_records= pd.DataFrame(category["id"])
    followers_list=[]

    for playlist_id in playlist_records["id"]:
       
        base_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        response = requests.get(base_url, headers=headers)
        
        if response.status_code == 200:
            playlists_data = response.json()
            followers_list.append(playlists_data["followers"]["total"])
      
        else:
            print("Error:", response.status_code)
    playlist_records["followers"]=followers_list
    return playlist_records