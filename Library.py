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
    # Group data: artist and album dictionary
    # album and the track dictionary
    # { artist, { album, { track, track } } }
    dictionaries = {}
    most_played = []
    artist_count = 0
    album_count = 0
    track_count = 0

    def __init__(self, file_name):
        with open(file_name, encoding='utf-8') as file:
            data = json.load(file)['tracks']  # we only care about tracks

        for elem in data:
            artist = elem['artist']
            album = elem['album']
            track = elem['track']

            if artist in self.dictionaries:
                if album not in self.dictionaries.get(artist):
                    # artist but no album
                    self. dictionaries[artist][album] = {}
                    self.album_count += 1
            else:
                # no artist no album
                self.dictionaries[artist] = {}
                self.dictionaries[artist][album] = {}
                self.album_count += 1
                self.artist_count += 1

            self.dictionaries[artist][album][track] = track
            self.track_count += 1

    def load_streaming_history(self, file_names):
        # Spotify decided to name
        # The House of the Rising Sun
        # and
        # The House Of The Rising Sun
        # elsewhere and things like that so we can't use the previous dictionary
        mostPlayedDict = {} # { artist, { trackName, msPlayed }}

        for file_name in file_names:
            with open(file_name, encoding='utf-8') as file:
                data = json.load(file)
                for elem in data:
                    artist_name = elem['artistName']
                    track_name = elem['trackName']
                    ms_played = elem['msPlayed']

                    if ms_played != 0:
                        if artist_name in mostPlayedDict:
                            if track_name not in mostPlayedDict.get(artist_name):
                                mostPlayedDict[artist_name][track_name] = 0
                        else:
                            mostPlayedDict[artist_name] = {}
                            mostPlayedDict[artist_name][track_name] = 0
                        mostPlayedDict[artist_name][track_name] += ms_played

        for artist, track_data in mostPlayedDict.items():
            for track_name, time in track_data.items():
                self.most_played.append((track_name, time, artist))

        self.most_played.sort(key=lambda track: track[1], reverse=True)

    def get_dict(self):
        return self.dictionaries

    def get_most_played(self):
        return self.most_played

    def get_stats(self):
        return self.artist_count, self.album_count, self.track_count
