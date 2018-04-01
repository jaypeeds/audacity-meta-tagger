#!/usr/bin/env python

import cgi, urllib2, json, sys, requests

reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2:
        sys.stderr.write('Usage: {} <artist> <album>\n'.format(sys.argv[0]))
        sys.exit(1)

artist = sys.argv[1]
album  = sys.argv[2]

if __name__ == '__main__':
    url = 'https://api.discogs.com/database/search?artist={}&release_title={}&country=france&per_page=5,&page=1&token=NqkWkULpPGcPEqpnyfvyvLcaEYuPlQpLtqEnLuli'.format(urllib2.quote(artist), urllib2.quote(album))
    print url
    req_headers = {'User-Agent': 'AudacityTaggerApp/3.0', 'Content-Encoding': 'gzip', 'Content-Type': 'application/json'} 

    response = requests.get(url, headers=req_headers).json()
    results = response.get('results')
    for result in results:
        print result.get("id")
