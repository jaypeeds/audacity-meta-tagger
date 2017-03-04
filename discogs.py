import urllib2, json, sys

release_id = int(sys.argv[1])
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'AudacityMetaTaggerApp/3.0')]
release = json.load(opener.open('https://api.discogs.com/releases/{}'.format(release_id)))

for artist in release['artists']:
	aname = artist['name']

album = release['title']
year= release['year']
for genre in release['genres']:
	gname = genre

asize = 0
for track in release['tracklist']:
	ttitle = track['title']
	chars = list(track['position'])
	if len(chars) == 2:
		[face, pos] = chars
	else:
		[face, pos10, pos ] = chars
		pos = 10 * int(pos10) + int(pos)

	if face == 'A':
		tposition = pos
		asize += 1
	else:
		tposition = asize + int(pos)

	file_name = '{}-{}-{}.xml'.format(aname,album,tposition)
	file_io = open(file_name, 'w')
	file_io.write( '<tags>\n' )
	file_io.write( '\t<tag name="GENRE" value="{}"/>\n'.format(gname) )
	file_io.write( '\t<tag name="TITLE" value="{}"/>\n'.format(ttitle))
	file_io.write( '\t<tag name="TRACKNUMBER" value="{}"/>\n'.format(tposition) )
	file_io.write( '\t<tag name="ALBUM" value="{}"/>\n'.format(album) )
	file_io.write( '\t<tag name="YEAR" value="{}"/>\n'.format(year) )
	file_io.write( '\t<tag name="ARTIST" value="{}"/>\n'.format(aname) )
	file_io.write( '</tags>\n' )
	file_io.close()

