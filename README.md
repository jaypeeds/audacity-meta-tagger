# audacity-meta-tagger
Script to generate tracks XML metadata to be used for Audacity multiple file export. 
If duration values are available they are used to generate a labels file for each side of the record, otherwise a standard length of 3 minutes is assumed, but generated file must be adjusted.

Usage
------
- Go to discogs.com site and search for the album you are digitizing
  - Many releases are available
  - Select your release
  - The release page URL ends with the release ID
- Use that ID on the command line: python discogs.py release_ID

Typical output
--------------
      $ ./discogs_search.py "Keith Jarrett" "Koln concert"
      4788677
      6988028
      9346057
      11563070
      11542483

      $ ./discogs.py 4788677
      Keith Jarrett-The Köln Concert-1.xml
      New side: labels for side 1 in Keith Jarrett-The Köln Concert-1.txt
      Keith Jarrett-The Köln Concert-2.xml
      New side: labels for side 2 in Keith Jarrett-The Köln Concert-2.txt
      Keith Jarrett-The Köln Concert-3.xml
      New side: labels for side 3 in Keith Jarrett-The Köln Concert-3.txt
      Keith Jarrett-The Köln Concert-4.xml
      Last side: labels for side 4 in Keith Jarrett-The Köln Concert-4.txt
      
