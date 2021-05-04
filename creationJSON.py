import os
import ipfsapi
import re
import json

#rename the images
dir_names=os.listdir("img")
img_ipfs_list=[]
list_files=list(range(0, len(dir_names)))
result=bool(re.search('DS', dir_names[2]))
okay_items = [item for item in dir_names if not bool(re.search('DS', item))]

okay_items= sorted(okay_items)

print(okay_items)

n=1
for i in okay_items:
    list_files=os.listdir('img/'+i)
    for y in list_files:
        os.rename('img/'+i+'/'+y, 'img/'+i+'/'+str(n)+'.png')
        n=n+1


exit()


def set_img_hashes():
    api = ipfsapi.Client('127.0.0.1', 5001)

    dir_names=os.listdir("img")
    img_ipfs_list=[]
    
    list_files=list(range(0, len(dir_names)))
    print(list_files)
    print(dir_names)
    result=bool(re.search('DS', dir_names[2]))

    okay_items = [item for item in dir_names if not bool(re.search('DS', item))]
    
    directory_number= [ dir_names.index(i) for i in okay_items if dir_names.index(i)]


    for i in okay_items:
        list_files=os.listdir('img/'+i)
        for y in list_files:
            res = api.add('img/'+i+'/'+y)
            img_ipfs_list.append(res)
            print(img_ipfs_list)
    
    return img_ipfs_list

img_hash_list= set_img_hashes()

f = open('json/list_ipfs.json', "w+")
f.write(json.dumps(img_hash_list))
f.close()

exit()

def set_json(img_ipfs_list):   
    
    author_list=["Titi","Toto","Tutu","Tata","Toutou","Tumtum","Tochtoch"]
    description="A lovely piece of art <3"
    author="0"
   
    
    i=0
    while (i<128):
        if i<8 :
            author=author_list[0]
        elif 8<=i<24 :
            author=author_list[1]
        elif 24<=i<48 :
            author=author_list[2]
        elif 48<=i<96 :
            author=author_list[3]
        elif 96<=i<120 :
           author=author_list[4] 
        elif 120<=i<136 :
            author=author_list[5] 
        else :
            author=author_list[6]
        
        a=str(img_ipfs_list[i])
        b=str(img_ipfs_list[i+1])
    
        txt='{\n "description": "'+description+'",\n "external_url": "https://gateway.pinata.cloud/ipfs/<hash>",\n "image": "https://ipfs.io/ipfs/'+a+'",\n "name": "'+b+'",\n "author": "'+author+'"\n }'
        
        file_name =b+'.json'
        f = open('json/'+file_name, "w+")
        f.write(txt)
        f.close()
        i=i+2


img_ipfs_list=set_img_hashes()
set_json(img_ipfs_list)

print("Finished")