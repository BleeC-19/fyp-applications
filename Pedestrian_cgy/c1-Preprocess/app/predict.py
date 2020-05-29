import numpy as np
import cv2
import time

def predict(image_index_str):
    start = time.time()
    image_path = "/container/data/" + image_index_str + " .png"
    #image_path = "../data/" + image_index_str + " .png"
    image = cv2.imread(image_path)
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (200, 200), interpolation=cv2.INTER_CUBIC)
    #cv2.imshow('dst',gray)
    #cv2.imshow('dst',gray)
    #cv2.waitKey(0)
    gray = cv2.cornerHarris(gray,2,3,0.04)
    print("resized shape", gray.shape)
    end = time.time()
    print("ELASPSED TIME", (end-start)*1000)
    return image_index_str



predict('2')

