import os
import ipfsapi
import re
import json

#rename the images
dir_names=os.listdir("img")
img_ipfs_list=[]
list_directories=list(range(0, len(dir_names)))
result=bool(re.search('DS', dir_names[2]))
okay_items = [item for item in dir_names if not bool(re.search('DS', item))]

okay_items= sorted(okay_items)

print(okay_items)

n=1
for i in okay_items:
    list_directories2=os.listdir('img/'+i)
    list_files= [y for y in list_directories2 if '.png' in y]
    list_files= sorted(list_files)
    for y in list_files:
        print('img/'+i+'/'+y)
        os.rename('img/'+i+'/'+y, 'img/'+i+'/'+str(n)+'.png')
        print('img/'+i+'/'+str(n)+'.png')
        n=n+1





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


print("Finished")