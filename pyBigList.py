#!/usr/bin/env python3
#pyBigList
import os, sys, gzip, wget, shutil
scriptPath = os.path.dirname(os.path.realpath(__file__))
blockList = '%s\\biglist.p2p' % scriptPath if sys.platform == 'win32' else '%s/biglist.p2p' % scriptPath
blockListGz = '%s\\biglist.p2p.gz' % scriptPath if sys.platform == 'win32' else '%s/biglist.p2p.gz' % scriptPath
blockListUrl = 'http://john.bitsurge.net/public/biglist.p2p.gz'
finalList = '/home/adam/Documents/biglist.p2p'

# remove old files
if os.path.isfile(blockList): os.remove(blockList)
if os.path.isfile(blockListGz): os.remove(blockListGz)
if sys.platform != 'win32' and os.path.isfile(finalList): os.remove(finalList)

# download the list
print('Downloading the list. . .')
wget.download(blockListUrl, blockListGz)

# decompress
print('\nDecompressing biglist.p2p.gz. . .')
with gzip.open(blockListGz, 'rb') as f_in:
    with open(blockList, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# copy the file to ~/Documents (if on linux)
if sys.platform != 'win32':
    print('Copying blocklist.p2p to ~/Documents.')
    shutil.copyfile(blockList, finalList)

# remove the gz file
print('Cleaning up. . .')
if os.path.isfile(blockListGz): os.remove(blockListGz)

# done!
print('Done!')
