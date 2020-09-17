# SpotifyData

## What does this program do?
This tool outputs some useful spotify stats (it's all based in liked songs and time spent listening to songs):

* All your tracks ordered by artist, album and song name in a recursive manner (check example below)
* Artist, album and track count
* Artists ordered by track count
* Artists ordered by time spent listening at them

## How to use the program

Make sure all the program .py files are in the same directory as YourLibrary.json.
If you also have StreamingHistoryX.json files drag them to the same directory.

For linux in the console run:
```
python3 Main.py 
```

## Introduction

When you download your spotify data found in https://www.spotify.com/es/account/privacy/ ("/es/" part might differ) the data is presented in JSON format.
It is interesting to see some of the data collected.

After some days you will get some files (I will skip some):
https://support.spotify.com/uk/account_payment_help/privacy/understanding-my-data/
* Playlist1.json (not used right now)
* Read_Me_First.pdf (they mention here that you can request more data)
* *StreamingHistory0.json*
* SearchQueries.json (all your searches)
* Userdata.json (creation date and more data)
* **YourLibrary.json**

Files in bold are required for the program to work, files in italics are optionally used by the program.

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

If you also supply some StreamingHistory.json files expect something along these lines:
```
Position     Seconds    Artist                                      Track name
       1	 554	Artist 1                                    Song 1
       2	 258	Artist 3            	                    Song 5
       3	   1	Artist 2                           	    Song 1
```

## License
This software is provided under the MIT License. Don't hesitate to contribute!

## TODO
* Better error checking
* Add some options