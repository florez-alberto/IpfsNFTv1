import os
import ipfsapi
import re
import json


dir_names=os.listdir("json")
okay_items = [item for item in dir_names if not bool(re.search('list', item))]

okay_items= sorted(okay_items)

print(okay_items)
list_ipfs= []

for i in okay_items:
    print(i)
    with open('json/'+i) as f:
        data = json.load(f)
    list_ipfs.append( {  "id":i[:-5],  "name": data["name"] ,"external_url":data["external_url"],"author": data["author"], "description": data["description"]})



f = open('nft-metadata.json', "w+")
f.write(json.dumps(list_ipfs))
f.close()

print("Finished")
