
import os
from PIL import Image
import re
import random

new_image = Image.new('RGB',(9*60, 8*60), (250,250,250))

dir_names=os.listdir("img")

list_files=list(range(0, len(dir_names)))
print(list_files)
print(dir_names)
dir_names=sorted(dir_names)
result=bool(re.search('DS', dir_names[2]))
okay_items = [item for item in dir_names if not bool(re.search('DS', item))]
    
directory_number= [ dir_names.index(i) for i in okay_items if dir_names.index(i)]

paths = []
for i in okay_items:
    list_files=os.listdir('img/'+i)
    for y in list_files:
        paths.append('img/'+i+'/'+y)

paths= random.sample(paths, len(paths))

path_index=0
image_y=0
for i in range(8):
    image_x= 0
    for n in range(9):
        image1 = Image.open(paths[path_index], 'r')
        path_index=path_index+1
        print(path_index)
        image1 = image1.resize((60, 60))
        new_image.paste(image1,(image_x,image_y))
        image_x= image_x+ 60
    image_y=image_y+60
    print(image_y)




new_image.save('img/collagetest.png')
