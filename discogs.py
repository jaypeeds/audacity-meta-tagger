#!/usr/bin/env python

import urllib2, json, sys

reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2:
        sys.stderr.write('Usage: {} <release ID>\n'.format(sys.argv[0]))
        sys.exit(1)

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

last_face = ''
end_ts = 0.0
labels = []
for track in release['tracklist']:
	tposition = track['position']	
	ttitle = track['title']
	tduration = track['duration']
	tface = list(tposition)[0]

	track_file_name = '{}-{}-{}.xml'.format(aname,album,tposition)


	if tduration != '':
		[mm, ss] = tduration.split(':')
	else:
		[mm, ss] = ['3', '0']
	
	
	if tface != last_face:
		if last_face != '':
			labels_file_name = '{}-{}-{}.txt'.format(aname,album,last_face)
			print 'New face: labels for face {} in {}'.format(last_face, labels_file_name)
			labels_io = open(labels_file_name, 'w')

		
		for label in labels:
			if last_face != '':
				labels_io.write('{}\n'.format(label))

		if last_face != '':
			labels_io.close()

		labels = []
		last_face = tface
		end_ts = 0.0

	start_ts = end_ts
	end_ts += 60.0 * float(mm) + float(ss)  

	labels.append('{}\t{}\t{}'.format(start_ts, end_ts, ttitle))
	print track_file_name
	track_io = open(track_file_name, 'w')
	track_io.write( '<tags>\n' )
	track_io.write( '\t<tag name="GENRE" value="{}"/>\n'.format(gname) )
	track_io.write( '\t<tag name="TITLE" value="{}"/>\n'.format(ttitle))
	track_io.write( '\t<tag name="TRACKNUMBER" value="{}"/>\n'.format(tposition) )
	track_io.write( '\t<tag name="ALBUM" value="{}"/>\n'.format(album) )
	track_io.write( '\t<tag name="YEAR" value="{}"/>\n'.format(year) )
	track_io.write( '\t<tag name="ARTIST" value="{}"/>\n'.format(aname) )
	track_io.write( '</tags>\n' )
	track_io.close()

labels_file_name = '{}-{}-{}.txt'.format(aname,album,last_face)
print 'Last face: labels for face {} in {}'.format(last_face, labels_file_name)
labels_io = open(labels_file_name, 'w')
for label in labels:
	labels_io.write('{}\n'.format(label))

labels_io.close()


