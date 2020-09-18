## What does this program do?
This program converts the json data that can be downloaded from your profile into a more readable format.
Make sure to check the examples to see how the json data looks as well as the output.

This may be usefull if you want to migrate platforms or you just want a text file with the name of all of your liked songs.

The program outputs:

* All your tracks ordered alphabetically by artist, album and song name in a recursive manner (check the example below).
* Artist, album and track count.
* Artists ordered by liked songs count.
* Artists ordered by time spent listening at them.

## How to use the program

1. Download your data from https://www.spotify.com/es/account/privacy/ ("/es/" part might differ).
**You may have to wait several days**.
2. Make sure all the program .py files are in the **same directory** as YourLibrary.json.
If you also have StreamingHistory*.json files drag them to the same directory.
You shouldn't need to do any renaming as the program looks for "StreamingHistory*" files (it will match with StreamingHistory0.json, StreamingHistory1.json, ...).
YourLibrary.json is **required** for the program to run.
3. Run the program.

In linux run:
```
python3 Main.py 
```

## Example

Input file (YourLibrary.json):
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
Output file (Output.out):
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

If you also supply some StreamingHistory* files:
```
Position     Seconds    Artist                                      Track name
       1	 554	Artist 1                                    Song 1
       2	 258	Artist 3            	                    Song 5
       3	   1	Artist 2                           	    Song 1
```

## License
This software is provided under the MIT License. Don't hesitate to contribute!
