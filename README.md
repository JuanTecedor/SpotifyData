# SpotifyData

## TLDR
This tool outputs some spotify stats and all your songs ordered alphabetically as well as your top artists (the ones with more tracks).

## Introduction

When you download your spotify data found in https://www.spotify.com/es/account/privacy/ ("es" part might differ) the data is presented in JSON format.
It is interesting to see some of the data collected.

After some days you will get some files (I will skip empty and/or non-relevant):
https://support.spotify.com/uk/account_payment_help/privacy/understanding-my-data/
* Playlist1.json (not used right now)
* Read_Me_First.pdf (they mention here that you can request more data)
* StreamingHistory0.json (self-explanatory)
* SearchQueries.json (every search you made)
* Userdata.json (creation date and some more data)
* YourLibrary.json (this is the most interesting for this project ATM)

## What does it output?

Example input file (YourLibrary.json):
```
{
  "tracks": [
    {
      "artist": "Artist 3",
      "album": "Album 1",
      "track": "Song 5"
    },
    {
      "artist": "Artist 2",
      "album": "Album 1",
      "track": "Song 1"
    },
    {
      "artist": "Artist 1",
      "album": "Album 1",
      "track": "Song 1"
    },
    {
      "artist": "Artist 1",
      "album": "Album 1",
      "track": "Song 2"
    }
  ]
  // ...
}
```
Example output (Output.out):
```
Artist: Artist 1
	Album: Album 1
		Track: Song 1
		Track: Song 2

Artist: Artist 2
	Album: Album 1
		Track: Song 1

Artist: Artist 3
	Album: Album 1
		Track: Song 5


Artist count: 3
Album count: 3
Track count: 4

Position  Track count       Artist
         1         2		Artist 1
         2         1		Artist 3
         3         1		Artist 2
```

## How does it work?

Data is loaded into a dictionary with several dictionaries inside. A dictionary is used to avoid duplicates.
The main dictionary is an artist dictionary, each artist has a dictionary of albums and each album has a track dictionary.
For example, dict[artist][album][track] is the way to insert a track given artist, album, track names.

Then the dictionary is converted into a list and the list is sorted.

Next the topArtists list is calculated from the ordered list.

Finally, the data is printed.

## TODO
* General code cleanup
* List songs by time spent listening to them
* Error checking if the file doesn't exist
* Alignment is broken in the example in top artists
