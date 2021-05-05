import os
import ipfsapi
import re
import json



with open('json/list_ipfs.json') as f:
  data = json.load(f)


list_hashes=[ [y["Hash"],int(y["Name"][:-4])] for y in data]

def Sort(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    return(sorted(sub_li, key = lambda x: x[1]))    
  
# Driver Code


list_hashes= Sort(list_hashes)
print(list_hashes[0] )
list_hashes=[ y[0] for y in list_hashes]

author_list=["Papipaz", "Alberto", "Gamatar","JC","Freelancer", "Berserk", "Brotoshi", "Tchoco" , "Mlolotte", "NightlyCatGirl" , "OrionDeimos"]
descriptions=["The first ones","Algorithmic shuffling with fractals","First Farmers of the Galaxy","A lovely piece of art <3", "Various Collabs", "Fungi Bizare Ploriferarion Part 1" , "Legendaries"]
#author="0"
   
for i in range(0,72):
        print (i+1)
        name=str(i+1)
        if i<4 :
            author=author_list[0]
            description=descriptions[0]
        elif 4<=i<12 :
            author=author_list[0]
            description=descriptions[1]
        elif 12<=i<24:
            author=author_list[0]
            description=descriptions[2]
        elif 24<=i<48 :
            author=author_list[2]
            description=descriptions[3]
        elif 48<=i<60 :
           author=author_list[0] 
           description=descriptions[4]
        elif 60<=i<68 :
            author=author_list[7]
            description=descriptions[5] 
        elif 60<=i<72 :
            author=author_list[8]
            description=descriptions[6]
        print(author)
        print(description)
        txt='{ "description": "'+description+'", "external_url": "https://gateway.pinata.cloud/ipfs/'+list_hashes[i]+'", "image": "https://ipfs.io/ipfs/'+list_hashes[i]+'", "name": "'+name+'", "author": "'+author+'" }'
        #file_name =data[i]["Name"]+'.json'
        f = open('json/'+name+'.json', "w+")
        f.write(txt)
        f.close()
