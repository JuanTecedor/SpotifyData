# MIT License
#
# Copyright (c) 2020 Juan Tecedor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json


class Library:
    # Library data is stored in this dictionary
    # key = artist(str), value = another dict that contains: key = album(str), value = set of songs(str)
    # dictionaries[artist][album] returns a set of all songs given an artist and an album
    dictionaries = {}

    most_played = []
    artist_count = 0
    album_count = 0
    track_count = 0

    def __init__(self, file_name, streaming_filenames):
        json_data = None
        try:
            with open(file_name, encoding='utf-8') as file:
                json_data = json.load(file)['tracks']  # only need tracks
        except FileNotFoundError:
            print("ERROR 1:", file_name, "not found.")
            return
        except OSError:
            print("ERROR 2: Can't open", file_name, "does it have read permision?")
            return
        else:
            self._load_library(json_data)
            self._load_streaming_history(streaming_filenames)

    def _load_library(self, json_data):
        for elem in json_data:
            artist = elem['artist']
            album = elem['album']
            track = elem['track']

            if artist in self.dictionaries:
                if album not in self.dictionaries.get(artist):
                    # artist but no album
                    self.dictionaries[artist][album] = set()
                    self.album_count += 1
            else:
                # no artist no album
                self.dictionaries[artist] = {}
                self.dictionaries[artist][album] = set()
                self.album_count += 1
                self.artist_count += 1

            self.dictionaries[artist][album].add(track)
            self.track_count += 1

    def _load_streaming_history(self, file_names):
        # The House of the Rising Sun         in YourLibrary.json
        #           | <- here 'o' and 'O'
        # The House Of The Rising Sun         in StreamingHistoryX.json
        # We can't use the previous library dictionary

        # mostPlayedDict structure:
        # key = artist(str), value = another dictionary
        # structure of the second dict:  key = trackname(str), value = msPlayed
        # most_played_dict[artist][track] returns the msPlayed of a given artist and song
        most_played_dict = {}
        data = None

        for file_name in file_names:
            try:
                with open(file_name, encoding='utf-8') as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("ERROR 3:", file_name, "not found.")
            except OSError:
                print("ERROR 4: Can't open", file_name, "does it have read permision?")
            else:
                for elem in data:
                    artist_name = elem['artistName']
                    track_name = elem['trackName']
                    ms_played = elem['msPlayed']

                    if ms_played != 0:
                        if artist_name in most_played_dict:
                            if track_name not in most_played_dict.get(artist_name):
                                most_played_dict[artist_name][track_name] = 0
                        else:
                            most_played_dict[artist_name] = {}
                            most_played_dict[artist_name][track_name] = 0
                        most_played_dict[artist_name][track_name] += ms_played

        for artist, track_data in most_played_dict.items():
            for track_name, time in track_data.items():
                self.most_played.append((track_name, time, artist))

        self.most_played.sort(key=lambda track: track[1], reverse=True)

    def get_library_list(self):
        library_list = []
        # Converts the dictionary into a list
        for artist, artist_dic in self.dictionaries.items():
            new_album_list = []
            library_list.append([artist, new_album_list])
            for album, album_dic in artist_dic.items():
                new_track_list = []
                new_album_list.append([album, new_track_list])
                for track_name in album_dic:
                    new_track_list.append(track_name)
                # for track_name, track_data in album_dic.items():
                #     new_track_list.append(track_name)

        # Order the list
        library_list.sort()
        for artist, albums in library_list:
            albums.sort()
            for album, tracks in albums:
                tracks.sort()

        return library_list

    def get_top_artists_by_track_count(self):
        top_artists_by_track_count = []
        for artist, albums in self.dictionaries.items():
            n_tracks = 0
            for album, tracks in albums.items():
                for track in tracks:
                    n_tracks += 1
            top_artists_by_track_count.append((n_tracks, artist))

        top_artists_by_track_count.sort(reverse=True)
        return top_artists_by_track_count

    def get_most_played(self):
        return self.most_played

    def get_stats(self):
        return self.artist_count, self.album_count, self.track_count
