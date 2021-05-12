import os
import re
import json



with open('metadata_json_hash_list.json') as f:
  data = json.load(f)


list_hashes=[ [y["Hash"],int(y["Name"][:-5])] for y in data]
print(list_hashes)

def Sort(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    return(sorted(sub_li, key = lambda x: x[1]))    
  
# Driver Code


list_hashes= Sort(list_hashes)
print(list_hashes )
list_hashes=[ y[0] for y in list_hashes]
print(list_hashes )

f = open('metadata_json_hash_list.txt', "w+")
n=0
for i in list_hashes:
    txt= '"'+i+'",'
    if n%8==0:
      if n==0:
        f.write(txt)
      else:
        f.write(txt+"\n")
    else:
      f.write(txt)
    n=n+1


f.close()
