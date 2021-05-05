import os
import ipfsapi
import re
import json



with open('json/list_ipfs.json') as f:
  data = json.load(f)

list_hashes= [[int(data[y]["Name"][:-3]),data[y]["Hashes"]] for y in data]
print(list_hashes)
exit()
list_files= sorted(list_files)
author_list=["Papipaz", "Alberto", "Gamatar","JC","Freelancer", "Berserk", "Brotoshi", "Tchoco" , "Mlolotte", "NightlyCatGirl" , "OrionDeimos"]
descriptions=["The first ones","Algorithmic shuffling with fractals","First Farmers of the Galaxy","A lovely piece of art <3", "Various Collabs", "Fungi Bizare Ploriferarion Part 1" , "Legendaries"]
#author="0"
   
for i in range(0,72):
        print (i+1)
        if i<4 :
            author=author_list[0]
            description=descriptions[0]
            name=str(i+1)
        elif 4<=i<12 :
            author=author_list[0]
            description=descriptions[1]
            name=str(i+1)
        elif 12<=i<24:
            author=author_list[0]
            description=descriptions[2]
            name=str(i+1)
        elif 24<=i<48 :
            author=author_list[2]
            description=descriptions[3]
            name=data[i]["Name"][:-4]
        elif 48<=i<60 :
           author=author_list[0] 
           description=descriptions[4]
           name=data[i]["Name"][:-4]
        elif 60<=i<68 :
            author=author_list[7]
            description=descriptions[5] 
            name=data[i]["Name"][:-4]
        elif 60<=i<72 :
            author=author_list[8]
            description=descriptions[6]
            name=data[i]["Name"][:-4]
        print(author)
        print(description)
        txt='{ "description": "'+description+'", "external_url": "https://gateway.pinata.cloud/ipfs/'+data[i]["Hash"]+'", "image": "https://ipfs.io/ipfs/'+data[i]["Hash"]+'", "name": "'+name+'", "author": "'+author+'" }'
        #file_name =data[i]["Name"]+'.json'
        f = open('json/'+str(i+1)+'.json', "w+")
        f.write(txt)
        f.close()
