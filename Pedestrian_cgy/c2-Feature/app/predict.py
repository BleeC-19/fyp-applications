import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from hog import Hog_descriptor



def predict(image_index_str):
    img = cv2.imread('/container/data/' + image_index_str + ' .png', cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread('../data/' + image_index_str + ' .png', cv2.IMREAD_GRAYSCALE)
    cv2.resize(img, (360, 360))
    hog = Hog_descriptor(img, cell_size=2, bin_size=2)
    vector, image = hog.extract()
    #plt.imshow(image, cmap=plt.cm.gray)
    #plt.show()
    #cv2.imwrite('./Output/' + str(image_index_str) + ' .jpg', image)
    return image_index_str

predict(1000)