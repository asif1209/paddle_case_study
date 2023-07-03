import requests, pandas as pd


def get_spotify_playlists(category_id,limit,access_token)->pd.DataFrame:
    """Retrieves a specified number of playlists in the latin category"""
    headers = {
        "Authorization": f"Bearer {access_token}"  
    }
    params = {
        "limit": limit  # Adjust the number of playlists you want to retrieve
    }

    base_url = f"https://api.spotify.com/v1/browse/categories/{category_id}/playlists"
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        category=pd.DataFrame()
        columns= ["name","description", "id","snapshot_id","tracks"]
        
        playlists_data = response.json()
        playlists = playlists_data["playlists"]["items"]

        for playlist in playlists:
            df=pd.DataFrame([playlist[key] for key in columns]).transpose()  # Print playlist names
            df.columns=columns           
            df=pd.concat([df.drop(["tracks"],axis=1),df["tracks"].apply(pd.Series)], axis=1)
            df
            category=pd.concat([category,df],axis=0)
            category.reset_index(drop=True, inplace=True)
        
        category=category.rename(columns={"href":"tracks_url","total":"total_tracks"})
    else:
        print("Error:", response.status_code)
    return category