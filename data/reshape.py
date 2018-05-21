from PIL import Image
import os
import sys

# def get_imlist(path):
#     return[os.path.join(path,f) for f in os.listdir(path)]

# def change_size(path):
#     directorys=get_imlist(path)
#     for directory in directorys:
#         img=Image.open(directory)


files_dir="./gt/"
save_dir="./out_gt/"
filename = os.listdir(files_dir)
for name in filename:
    img=Image.open(files_dir + name)
    new_img = img.resize((108,108),Image.ANTIALIAS)
    # os.path.join(save_dir, new_img)
    new_img.save("./out_gt/" + name)

