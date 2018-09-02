year = 1967


with open('top-500.txt', 'r') as f:
    _lines = f.read().splitlines()

    # we remove the first line
    # which describes the fields
    lines = _lines[1:]


radiohead_albums = []
for line in lines:
    number, year, album, artist, genre, subgenre = tuple(line.split(';'))
    if artist == 'Radiohead':
        radiohead_albums.append(album)


print('Radiohead albums:', radiohead_albums)


beatles_albums = []
for line in lines:
    number, year, album, artist, genre, subgenre = tuple(line.split(';'))
    if artist == 'The Beatles':
        beatles_albums.append(album)


print('\nBeatles albums:', beatles_albums)


num_albums = {}
for line in lines:
    year = line.split(';')[1]
    year = int(year)
    if year in num_albums:
        num_albums[year] += 1
    else:
        num_albums[year] = 1


print('\nyears and how many albums in that year:')
print(num_albums)

# TODO would be nice to plot a histogram (ascii or actual plot)


print()
print(num_albums[year], 'albums from year', year)
