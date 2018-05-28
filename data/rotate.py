import numpy as np 
from PIL import Image
import os 

# read_dir = "./joined_input_frame/"

# for file in os.listdir(read_dir):
#     filename = os.path.splitext(file)[0]
#     array = np.load(read_dir+file)
#     for i in range(1,4):
#         new_array = np.rot90(array, i)
#         np.save(read_dir+filename+"_"+str(i)+".npy", new_array)

gt_dir = "./gt/"

for file in os.listdir(gt_dir):
    filename = os.path.splitext(file)[0]
    img = Image.open(gt_dir+file)
    for i in range(1,4):
        new_img = img.rotate(90*i)
        new_img.save(gt_dir+filename+"_"+str(i)+".jpg")