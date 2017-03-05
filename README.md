# audacity-meta-tagger
Script to generate tracks XML metadata to be used for Audacity multiple file export
If duration values are available they are used to generate a labels file for each side of the record, otherwise a standard length of 3 minutes is assumed, but generated file must be adjusted.

Usage
------
- Go to discogs.com site and search for the album you are digitizing
  - Many releases are available
  - Select you release
  - The release page URL ends with the release ID
- Use that ID on the command line: python discogs.py release_ID

    [jaypee:.../Tags & Labels for Audacity]$ ./discogs.py 3458476                                                     
    Stevie Wonder-Journey Through The Secret Life Of Plants-A1.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-A2.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-A3.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-A4.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-A5.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-A6.xml
    New face: labels for face A in Stevie Wonder-Journey Through The Secret Life Of Plants-A.txt
    Stevie Wonder-Journey Through The Secret Life Of Plants-B1.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-B2.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-B3.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-B4.xml
    New face: labels for face B in Stevie Wonder-Journey Through The Secret Life Of Plants-B.txt
    Stevie Wonder-Journey Through The Secret Life Of Plants-C1.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-C2.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-C3.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-C4.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-C5.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-C6.xml
    New face: labels for face C in Stevie Wonder-Journey Through The Secret Life Of Plants-C.txt
    Stevie Wonder-Journey Through The Secret Life Of Plants-D1.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-D2.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-D3.xml
    Stevie Wonder-Journey Through The Secret Life Of Plants-D4.xml
    Last face: labels for face D in Stevie Wonder-Journey Through The Secret Life Of Plants-D.txt
