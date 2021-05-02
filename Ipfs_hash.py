import os
import ipfsapi
import json

def set_img_hashes():
    api = ipfsapi.Client('127.0.0.1', 5001)
    

    dir_names=os.listdir("img")
    img_ipfs_list=[]
    
    list_files=list(range(0, len(dir_names)))
    
    for i in range (0,len(dir_names)):
        list_files[i]=os.listdir('img/'+ str(i)+dir_names[i])
        
        for y in range (0,len(list_files[i])):
            a=api.add('img/'+dir_names[i]+'/'+list_files[i][y])
            img_ipfs_list.extend((a[0]['Hash'],list_files[i][y]))
    
    return img_ipfs_list

image_hashes= set_img_hashes()
print(image_hashes)

f = open('json/'+ listofNFTs.txt, "w+")
f.write(image_hashes)
f.close()

file_name =n+'.json'
f = open('json/'+ listofNFTs.json, "w+")
f.write(json(image_hashes))
f.close()


