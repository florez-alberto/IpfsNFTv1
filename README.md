# Ipfs

To use these scripts, you need:

-ipfsapi on python (pip install ipfsapi)

-Ipfs serveur (IPFS Desktop, for instance)

For this version: 

First, creationJSON.py uploads all the files in "img" directory into IPFS. Then it stores the information of this upload in json/list_ipfs.json
Then pinatapinner will take the hashes and pin them in your personal pinata account. I already revoked the api keys so you have to generate your own. 
Then, pinnedHashToJson creates the JSON metadata. This is still in works because the metadata order is messed up.
Finally the creationJSON should take care of uplading it to ipfs, and then a similar script as pinatapinner should finish the job and return a list with the pinned ipfs hashes for this json.


