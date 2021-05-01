import os
import ipfsApi


api = ipfsApi.Client('127.0.0.1', 5001)


json_files =os.listdir("json")
img_ipfs_list=[]

list_files=list(range(0, len(json_files)))

file_name ="metadata_json_hash_list.txt"
f = open(file_name, "r+")

for i in range (0,len(list_files)):
    
        a=api.add('json/'+json_files[i])

        f.write(str(a[0]['Hash'])+"\n")


f.close()

print("Finished")
        