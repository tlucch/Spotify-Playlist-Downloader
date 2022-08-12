# Spotify-Playlist-Downloader

### Simple Description

A set of simple Python functions that helps us download all tracks from a Spotify playlist to .mp3 format

### Necessary Libraries

* `pip install spotipy` : A library that helps us connect and play with the Spotify API
* `pip install youtube_search` : A library that helps us making searches in youtube
* `pip install youtube_dl` : A library that helps us downloading music from youtube

### Functions

***IMPORTANT: Im still working in this section of the doc. Meanwhile you can find all the needed info in the comments made in the code***

The code consist of 4 simple Python functions:

  * `spotify_get_names()` : This function searches a track in youtube and returns a list of the results info
  * `youtube_search()` : This function searches a track in youtube and returns a list of the results info
  * `get_best()` : This function gets the youtube URL of the best result for the searches made by the "youtube_search()" function
  * `youtube_to_wav()` : This function uses a youtube URL to download an MP3 of the video

At the end you can find and extra function with no name two show you and example of how you can implement this functions all together to download many playlist into different folders in your computer
