# Ipfs

To use these scripts, you need:

-ipfsapi on python (pip install ipfsapi)

-Ipfs serveur (IPFS Desktop, for instance)

First, creationJSON.py uploads all the files in "img" directory into IPFS. It gets the ipfs hashes and creates metadata json. These json can be seen into "json" directory.

Then, creationFinalHashList.py uploads the json on IPFS and creates a list,"metadata_json_hash_list.txt", that has all the json hashes from ipfs. 

