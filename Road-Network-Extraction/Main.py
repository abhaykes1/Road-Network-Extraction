import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
epsilon = 40

'''Reading Image'''

imgPath = "./images/input2.png"
image = cv.imread(imgPath, 1)
cv.imshow('original image', image)
image_gray = cv.imread(imgPath, 0)
#converting images to 0-1 intensity values
image = image/255


'''Segmentation'''

# reshape 3 channel image into 2d space
pic_n = image.reshape(image.shape[0]*image.shape[1], image.shape[2])
# segment image into 4 clusters
kmeans = KMeans(n_clusters=4, random_state=0).fit(pic_n)
pic2show = kmeans.cluster_centers_[kmeans.labels_]
# reshape image to its original shape
cluster_pic = pic2show.reshape(image.shape[0], image.shape[1], image.shape[2])

# converting segmented image back to 0-255 intensity values
cluster_pic = cluster_pic*255
cluster_pic = np.uint8(cluster_pic)
img = cluster_pic


'''Grayscale image'''

# converting colour scale of image
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray_image", img)
histogram = cv.calcHist([img], [0], None, [256], [0, 256])
# finding intensity with max probability in histogram
maxIntensity = np.where(histogram == np.amax(histogram))[0][0]


'''Epsilon-Thresholding'''

# reshape 2D grayscale image into 1D array
gray_r = img.reshape(img.shape[0] * img.shape[1])
for i in range(gray_r.shape[0]):
    # level threshold peak intensity and its epsilon-neighbour to 255
    if abs(gray_r[i] - maxIntensity) <= epsilon:
        gray_r[i]=255
    else:
        gray_r[i]=0
img = gray_r.reshape(img.shape[0], img.shape[1])
t = img
cv.imshow('thresholding', t)


'''edge detection'''

# Using laplacian method to detect edges
edges = cv.Laplacian(img, cv.CV_64F)
cv.imshow('Edge detection', edges)

'''Overlay Extracted road image over original BnW image'''

overlay = cv.addWeighted(image_gray, 0.5, edges.astype(np.uint8), 0.5, 0)
cv.imshow('Overlay Image',overlay)


cv.waitKey(0)
cv.destroyAllWindows()

