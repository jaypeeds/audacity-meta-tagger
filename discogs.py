#!/usr/bin/env python

import urllib2, json, sys
from xml.sax.saxutils import escape

reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2:
        sys.stderr.write('Usage: {} <release ID>\n'.format(sys.argv[0]))
        sys.exit(1)

last_side = ''
end_ts = 0.0
labels = []
offset = 0

def quote_escape(text):
    return escape(text, {"'": "&apos;", '"': "&quot;"})

def track_name_to_number(tname):
    # Valid names:
    # A
    # A1
    # A.a
    if tname.isnumeric():
        return int(tname)
    else:
        if '.' in tname:
            name = list(tname.split('.')[1])
        else:
            name = list(tname)
        return ord(name[0]) - ord('a') + 1


def process_track(track):

	global last_side
        global end_ts
        global labels
        global offset

        tposition = [track['position'][0], track['position'][1:]]	
	ttitle = track['title']
	tduration = track['duration']
	tside = list(tposition)[0]


	if tduration != '':
		[mm, ss] = tduration.split(':')
	else:
		[mm, ss] = ['3', '0']
	
	
	if tside != last_side:
		if last_side != '':
			labels_file_name = '{}-{}-{}.txt'.format(aname,album,last_side)
			print 'New side: labels for side {} in {}'.format(last_side, labels_file_name)
			labels_io = open(labels_file_name, 'w')

		
		for label in labels:
			if last_side != '':
				labels_io.write('{}\n'.format(label))

		if last_side != '':
			offset += len(labels)
			labels_io.close()

		labels = []
		last_side = tside
		end_ts = 0.0

	start_ts = end_ts
	end_ts += 60.0 * float(mm) + float(ss)  

	labels.append('{}\t{}\t{}'.format(start_ts, end_ts, ttitle))
    	# Such records as Keith Jarrett's Koeln Concert have one track per side: A, B, C, D
    	# So A is equivalent to A1
    	try:	
        	track_number = offset + track_name_to_number(tposition[1]) 
    	except:
        	track_number = offset + 1
        
	track_file_name = '{}-{}-{}.xml'.format(aname,album,track['position'])
	print track_file_name
	track_io = open(track_file_name, 'w')
	track_io.write( '<tags>\n' )
	track_io.write( '\t<tag name="GENRE" value="{}"/>\n'.format(quote_escape(gname)) )
	track_io.write( '\t<tag name="TITLE" value="{}"/>\n'.format(quote_escape(ttitle)) )
	track_io.write( '\t<tag name="TRACKNUMBER" value="{}"/>\n'.format(track_number) )
	track_io.write( '\t<tag name="ALBUM" value="{}"/>\n'.format(quote_escape(album)) )
	track_io.write( '\t<tag name="YEAR" value="{}"/>\n'.format(year) )
	track_io.write( '\t<tag name="ARTIST" value="{}"/>\n'.format(quote_escape(aname)) )
	track_io.write( '</tags>\n' )
	track_io.write( '<!-- Generated from discogs release ID {} -->\n'.format(release_id) )
	track_io.close()



if __name__ == '__main__':
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
        track_type = track['type_']
        if track_type == 'track':
            process_track(track)
        elif track_type == 'index':
            sub_tracks = track['sub_tracks']
            for sub_track in sub_tracks:
                process_track(sub_track)
	else:
	    continue

    labels_file_name = '{}-{}-{}.txt'.format(aname,album,last_side)
    print 'Last side: labels for side {} in {}'.format(last_side, labels_file_name)
    labels_io = open(labels_file_name, 'w')
    for label in labels:
            labels_io.write('{}\n'.format(label))

    labels_io.close()

