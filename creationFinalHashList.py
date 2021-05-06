import os
import ipfsapi
import re
import json

api = ipfsapi.Client('127.0.0.1', 5001)

json_files =os.listdir("json")

okay_items = [item for item in json_files if not bool(re.search('list', item))]


json_ipfs_list=[]

for i in okay_items:
        print(i)
        res=api.add('json/'+i)
        json_ipfs_list.append(res)



f = open('metadata_json_hash_list.json', "w+")
f.write(json.dumps(json_ipfs_list))
f.close()

print("Finished")
