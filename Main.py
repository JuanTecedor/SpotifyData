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
import glob
from Library import *


def get_filenames():
    print('Please drag all the files into the executable directory.')
    print('At least a "YourLibrary.json" should be present')
    print('Program will also add "StreamingHistory*"')
    print('This works with StreamingHistory1.json, StreamingHistory2.json, ...')
    input('Press Enter to continue...')

    default_library_filename = 'YourLibrary.json'

    streaming_filenames = []
    for file in glob.glob('StreamingHistory*'):
        streaming_filenames.append(file)

    return default_library_filename, streaming_filenames


def print_output(library_list, most_played, top_artists_by_track_count,
                 artist_count, album_count, track_count):
    # OUTPUT
    # Characters like řá were causing problems in W10 so we use utf-8-sig
    with codecs.open('Output.out', 'w', 'utf-8-sig') as output_file:
        # Print main chunk of data
        for artist, album_list in library_list:
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
        for tracks, artist in top_artists_by_track_count:
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


def main():
    library_file_name, streaming_filenames = get_filenames()

    lib = Library(library_file_name)
    lib.load_library()

    artist_count, album_count, track_count = lib.get_stats()

    lib.load_streaming_history(streaming_filenames)
    most_played = lib.get_most_played()

    library_list = lib.get_library_list()

    # Calculate top artists
    top_artists_by_track_count = []
    for artist, albums in library_list:
        n_tracks = 0
        for album, tracks in albums:
            for track in tracks:
                n_tracks += 1
        top_artists_by_track_count.append((n_tracks, artist))

    top_artists_by_track_count.sort(reverse=True)

    print_output(library_list, most_played, top_artists_by_track_count,
                 artist_count, album_count, track_count)


if __name__ == '__main__':
    main()
