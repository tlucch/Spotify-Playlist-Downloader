#necesarry to run the code
from __future__ import unicode_literals

#----------------------------------------------------------

#This function conects to the Spotify API and returns a list of all the names and artist of the tracks in the playlist in the following format "track - artist"
#You have to introduce the spotify developer cid and secret code and the playlist_link
def spotify_get_names(cid, secret, playlist_link):
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    global tracks
    tracks = []
    
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        
        track_name = track["track"]["name"]
    
        artist = track["track"]["artists"][0]["name"]
         
        tracks.append(artist + " - " + track_name )

#----------------------------------------------------------

#This function searches a track in youtube and returns a list of the results info
#The "max_results" variable establishes how many results you want to get. By default is set to return the fisrt 3 results
def youtube_search(track, max_results = 3):
    from youtube_search import YoutubeSearch

    global results
    results = YoutubeSearch(track, max_results=max_results).to_dict()
    
#----------------------------------------------------------

#This function gets the youtube URL of the best result for the searches made by the "youtube_search()" function.
#less_hour variable difines if your will accept videos with a duration smaller than an hour. By default is set to True, this means it will discard all videos with a duration longer than an hour
#if less_hour is set to True, you can use the "duration_minutes" variable to establish the max duration of minutes you want the video to be. By default is set to 20 minutes
#if less_hour is set to False, you can use the "duration_hours" variable to establish the max duration of hours you want the video to be. By default is set to 1 hour
def get_best(results, less_hour = True, duration_minutes = 20, duration_hours = 1):
    
    global url
    
    url = ""
    biggest_views = 0
    
    for video in results:
        
        if len(video["duration"].split(":")) >= 3 and less_hour == True:
            continue
        
        if int(video["views"][:-7].replace(",","")) > biggest_views:
            if int(video["duration"].split(':')[0]) < duration_minutes and less_hour == True:
                biggest_views = int(video["views"][:-7].replace(",",""))
                url = 'https://www.youtube.com' + video['url_suffix']
            elif int(video["duration"].split(":")[0]) <= duration_hours and less_hour == False:
                biggest_views = int(video["views"][:-7].replace(",",""))
                url = 'https://www.youtube.com' + video['url_suffix']
            
#----------------------------------------------------------

#This function uses a youtube URL to download an MP3 of the video
#The "track" variable is the name you want the downloaded file to have
#The "folder" is the path of the folder you want the files to be dowloaded into. By default is set to be downloaded into the the same folder were this code is saved 
def youtube_to_wav(url, track, folder = None):
    import youtube_dl
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = url,download=False
    )
    filename = f"{track}.mp3"
    if folder == None:
        outtmpl = filename
    else:
        outtmpl = f"{folder}\{filename}"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl': outtmpl,
        'audioformat' : "mp3"
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


#----------------------------------------------------------

#This is an example of how to use all the functions in order to download many playlist into different folders

#You establish your cid and secret code
cid= "Enter your Spotify Developer Cid"
secret = "Enter your Spotify Developer Secret"

#You create a list of lists containing the playlist link and the folder you want to save that list. An example is given below (Viva los ritmos latinos!)
playlists = [["https://open.spotify.com/playlist/0FfcxKXQuJoMnqYGW0qn7s?si=03e51aca6a6240c8", "C:/Salsa"], ["https://open.spotify.com/playlist/37i9dQZF1DWWU6Rfto8Ppm?si=4b5708d329bb4f1e", "C:/Reggaeton Viejo"]]

#As you can see, I've added a count to keep a track of how many songs have been downloaded out of the total
for playlist_link in playlists:           
    spotify_get_names(cid, secret, playlist_link[0])
    count = 0
    for track in tracks:
        try:
            count += 1
            youtube_search(track)
            get_best(results)
            youtube_to_wav(url, track, playlist_link[1])
            print("Completed: ", count,"/",len(tracks))
        except:
            count += 1
            print("Could not download: {track}")
            
        
        
        
        
        
        
        
        
        