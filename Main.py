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

import codecs
from Library import *


def main():
    file_name = ''
    default_file_name = 'YourLibrary.json'

    file_name = input('Enter file name (empty for default ' + default_file_name + '):')
    if file_name == '':
        file_name = default_file_name

    lib = Library(file_name)
    dictionaries = lib.get_dict()
    artist_count, album_count, track_count = lib.get_stats()

    # TODO
    lib.load_streaming_history(['StreamingHistory0.json', 'StreamingHistory1.json', 'StreamingHistory2.json'])
    most_played = lib.get_most_played()

    # Convert dictionary into a list
    ordered = []
    for artist, artist_dic in dictionaries.items():
        new_album_list = []
        ordered.append([artist, new_album_list])
        for album, album_dic in artist_dic.items():
            new_track_list = []
            new_album_list.append([album, new_track_list])
            for track_name, track_data in album_dic.items():
                new_track_list.append(track_name)

    # Sort the list
    ordered.sort()
    for artist, albums in ordered:
        albums.sort()
        for album, tracks in albums:
            tracks.sort()

    # Calculate top artists
    top_artists_track_count = []
    for artist, albums in ordered:
        n_tracks = 0
        for album, tracks in albums:
            for track in tracks:
                n_tracks += 1
        top_artists_track_count.append((n_tracks, artist))

    top_artists_track_count.sort(reverse=True)

    # OUTPUT
    # Characters like řá were causing problems in W10 so we use utf-8-sig
    with codecs.open('Output.out', 'w', 'utf-8-sig') as output_file:
        # Print main chunk of data
        for artist, album_list in ordered:
            output_file.write(('Artist: ' + artist + '\n'))
            for album, track_list in album_list:
                output_file.write('\tAlbum: ' + album + '\n')
                for track in track_list:
                    output_file.write('\t\tTrack: ' + track + '\n')
            output_file.write('\n')

        # Print top artists by track count
        output_file.write('\nArtist count: ' + str(artist_count) + '\n')
        output_file.write('Album count: ' + str(album_count) + '\n')
        output_file.write('Track count: ' + str(track_count) + '\n\n')

        output_file.write('Position       Track count          Artist\n')
        i = 1
        for tracks, artist in top_artists_track_count:
            output_file.write(
                str('{:15}'.format(i)) + str('{:15}'.format(tracks)) + '\t\t' +
                str('{:15}'.format(artist)) + '\n'
            )
            i += 1
        output_file.write('\n\n')

        output_file.write('Position     Seconds    Artist          ' +
                          '                            Track name\n')
        i = 1
        for track_name, ms_played, artist in most_played:
            output_file.write(
                str('{:8}'.format(i)) + '\t' + str('{:8}'.format(ms_played // 1000)) + '\t' +
                str('{:40}'.format(artist)) + '\t' + track_name + '\n'
            )
            i += 1
        output_file.write('\n\n')


if __name__ == '__main__':
    main()
