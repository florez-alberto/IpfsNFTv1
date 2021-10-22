


author_list=["Papipaz", "Alberto", "Gamatar","JC","Freelancer", "Berserk", "Brotoshi", "Tchoco" , "Mlolotte", "NightlyCatGirl" , "OrionDeimos"]
descriptions=["The first ones","Algorithmic shuffling with fractals","First Farmers of the Galaxy","A lovely piece of art <3", "Various Collabs", "Fungi Bizare Ploriferarion Part 1" , "Legendaries"]
#author="0"
list_metadata=[]
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
        txt={ "id": name,  "description": description, "external_url": "/img/"+str(name)+".png","compressed_url":"/compressed-nfts/"+str(name)+"-min.png", "name":name, "author": author }
        list_metadata.append(txt)

print(list_metadata)

file_name ="compressed_metadata.json"
f = open(file_name, "w+")
f.write(str(list_metadata))
f.close()

