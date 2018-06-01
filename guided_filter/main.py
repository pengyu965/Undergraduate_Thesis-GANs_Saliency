import cv2
import numpy as np
import itertools
import sys
import os
from PIL import Image

from core.filter import GuidedFilter
from tools import visualize as vis
from cv.image import to_8U, to_32F

read_dir = "./test_result/"
save_dir = "./test_result_guided/"

for file in os.listdir(read_dir):

    image = cv2.imread(read_dir + file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # radius = [2, 4, 8]
    # eps = [0.1**2, 0.2**2, 0.4**2]
    radius = 4
    eps = 0.4**2


    GF = GuidedFilter(image, radius=radius, eps=eps)
    Image.fromarray(GF.filter(image)*255).convert("L").save(save_dir+file)
    
    



# def test_color():
#     image = cv2.imread('data/Lenna.png')
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     noise = (np.random.rand(image.shape[0], image.shape[1], 3) - 0.5) * 50
#     image_noise = image + noise

#     radius = [1, 2, 4]
#     eps = [0.005]

#     combs = list(itertools.product(radius, eps))

#     vis.plot_single(to_32F(image), title='origin')
#     vis.plot_single(to_32F(image_noise), title='noise')

#     for r, e in combs:
#         GF = GuidedFilter(image, radius=r, eps=e)
#         vis.plot_single(to_32F(GF.filter(image_noise)), title='r=%d, eps=%.3f' % (r, e))