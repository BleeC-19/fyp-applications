import numpy as np
import cv2
import time

def keras_process_image(img):
    image_x = 40
    image_y = 40
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    return img

def read_image(i):
    image_path = "/container/data/" + i + " .png"
    image = cv2.imread(image_path)
    print("original shape", image.shape)
    return image

def predict(image_index_str):
    try:
        start = time.time()
        image = read_image(image_index_str)
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
    except Exception as exc:
        print('Generated an exception: %s' % (exc))

if __name__ == "__main__":
    predict(2)


