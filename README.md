# audacity-meta-tagger
Script to generate tracks XML metadata to be used for Audacity multiple file export. 
If duration values are available they are used to generate a labels file for each side of the record, otherwise a standard length of 3 minutes is assumed, but generated file must be adjusted.

Usage
------
- Go to discogs.com site and search for the album you are digitizing
  - Many releases are available
  - Select you release
  - The release page URL ends with the release ID
- Use that ID on the command line: python discogs.py release_ID

Typical output
--------------
      $ ./discogs.py 385671                       
      Keith Jarrett-The Köln Concert-A.xml
      New face: labels for face A in Keith Jarrett-The Köln Concert-A.txt
      Keith Jarrett-The Köln Concert-B.xml
      New face: labels for face B in Keith Jarrett-The Köln Concert-B.txt
      Keith Jarrett-The Köln Concert-C.xml
      New face: labels for face C in Keith Jarrett-The Köln Concert-C.txt
      Keith Jarrett-The Köln Concert-D.xml
      Last face: labels for face D in Keith Jarrett-The Köln Concert-D.txt
