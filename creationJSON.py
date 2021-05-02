import os
import ipfshttpclient


client = ipfshttpclient.connect()

def set_img_hashes():
    

    dir_names=os.listdir("img")
    img_ipfs_list=[]
    
    list_files=list(range(0, len(dir_names)))
    print(list_files)
    
    #for i in range (0,len(dir_names)):
     #   print(dir_names)
      #  list_files[i]=os.listdir('img/'+dir_names[i])

        
       # for y in range (0,len(list_files[i]))
        #    res = client.add('img/'+dir_names[i]+'/'+list_files[i][y])
         #   img_ipfs_list.extend(client.cat(res['Hash']))
    
    #return img_ipfs_list
    
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