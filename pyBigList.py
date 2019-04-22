#!/usr/bin/env python3
#pyBigList
import os, sys, gzip, wget, shutil
scriptPath = os.path.dirname(os.path.realpath(__file__))
blockList = '%s\\biglist.p2p' % scriptPath if sys.platform == 'win32' else '%s/biglist.p2p' % scriptPath
blockListGz = '%s\\biglist.p2p.gz' % scriptPath if sys.platform == 'win32' else '%s/biglist.p2p.gz' % scriptPath
blockListUrl = 'http://john.bitsurge.net/public/biglist.p2p.gz'
finalList = os.path.expanduser('~/Documents/biglist.p2p') if sys.platform != 'win32' else '/dev/null'

# remove old files
if sys.platform == 'win32':
    if os.path.isfile(blockList): os.remove(blockList)
else:
    if os.path.isfile(finalList): os.remove(finalList)
if os.path.isfile(blockListGz): os.remove(blockListGz)

# download the list
print('Downloading the list. . .')
wget.download(blockListUrl, blockListGz)

# decompress
print('\nDecompressing biglist.p2p.gz. . .')
with gzip.open(blockListGz, 'rb') as f_in:
    with open(blockList if sys.platform == 'win32' else finalList, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# remove the gz file
print('Cleaning up. . .')
if os.path.isfile(blockListGz): os.remove(blockListGz)

# done!
print('Done!')
