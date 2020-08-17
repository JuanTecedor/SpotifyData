import codecs
import json


def main():
    file_name = ''
    default_file_name = 'YourLibrary.json'

    file_name = input('Enter file name (empty for default ' + default_file_name + '):')
    if file_name == '':
        file_name = default_file_name

    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)['tracks']  # we only care about tracks

    # Group data: artist and album dictionary
    # album and the track dictionary
    # { artist, { album, { track, track } } }
    dictionaries = {}
    artistCount = 0
    albumCount = 0
    trackCount = 0

    for elem in data:
        artist = elem['artist']
        album = elem['album']
        track = elem['track']

        if artist in dictionaries:
            if album not in dictionaries.get(artist):
                # artist but no album
                dictionaries[artist][album] = {}
                albumCount += 1
        else:
            # no artist no album
            dictionaries[artist] = {}
            dictionaries[artist][album] = {}
            albumCount += 1
            artistCount += 1

        dictionaries[artist][album][track] = track
        trackCount += 1

    # Convert dictionary into a list
    ordered = []
    for artist, artist_dic in dictionaries.items():
        new_album_list = []
        ordered.append([artist, new_album_list])
        for album, album_dic in artist_dic.items():
            new_track_list = []
            new_album_list.append([album, new_track_list])
            for track in album_dic:
                new_track_list.append(track)

    # Sort the list
    ordered.sort()
    for artist, albums in ordered:
        albums.sort()
        for album, tracks in albums:
            tracks.sort()

    # Calculate top artists
    topArtists = []
    for artist, albums in ordered:
        artistTracks = 0
        for album, tracks in albums:
            for track in tracks:
                artistTracks += 1
        topArtists.append((artistTracks, artist))
        
    topArtists.sort(reverse= True)

    # OUTPUT
    # Characters like řá were causing problems in W10 so we use utf-8-sig
    with codecs.open('Output.out', 'w', 'utf-8-sig') as output_file:
        for artist, album_list in ordered:
            output_file.write(('Artist: ' + artist + '\n'))
            for album, track_list in album_list:
                output_file.write('\tAlbum: ' + album + '\n')
                for track in track_list:
                    output_file.write('\t\tTrack: ' + track + '\n')
            output_file.write('\n')

        output_file.write('\nArtist count: ' + str(artistCount) + '\n')
        output_file.write('Album count: ' + str(albumCount) + '\n')
        output_file.write('Track count: ' + str(trackCount) + '\n\n')

        output_file.write('Position  Track count       Artist\n')
        i = 1
        for tracks, artist in topArtists:
            output_file.write(str('{:10}'.format(i)) + str('{:10}'.format(tracks)) + '\t\t' + artist + '\n')
            i += 1


if __name__ == '__main__':
    main()
