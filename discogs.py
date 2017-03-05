#!/usr/bin/env python

import urllib2, json, sys

reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2:
     raise RuntimeError('USAGE: %s <discogs release id>')
 
release_id = int(sys.argv[1])

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'AudacityTaggerApp/3.0'), ('Content-Encoding', 'gzip')]
json_response = opener.open('https://api.discogs.com/releases/{}'.format(release_id)) 

release = json.load(json_response)

for artist in release['artists']:
	aname = artist['name']

album = release['title']
year= release['year']
for genre in release['genres']:
	gname = genre

for track in release['tracklist']:
	ttitle = track['title']
	tposition = track['position']
	file_name = '{}-{}-{}.xml'.format(aname,album,tposition)
	print file_name
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

