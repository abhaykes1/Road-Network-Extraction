import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from sklearn.cluster import KMeans
epsilon = 40

# use original2, original4, original to test algorithm
#Reading Image
imgPath = "./images/original.png"
image = cv.imread(imgPath, 1)
image_gray = cv.imread(imgPath, 0)
outputs = [image]
image = image /255
titles = ["original"]


#Segmentation
pic_n = image.reshape(image.shape[0]*image.shape[1], image.shape[2])
kmeans = KMeans(n_clusters=4, random_state=0).fit(pic_n)
pic2show = kmeans.cluster_centers_[kmeans.labels_]
cluster_pic = pic2show.reshape(image.shape[0], image.shape[1], image.shape[2])
# cv.imshow('segmented0',cluster_pic)
outputs.insert(len(outputs), cluster_pic);
titles.insert(len(outputs), "segmented");
cluster_pic = cluster_pic*255
cluster_pic = np.uint8(cluster_pic)
img = cluster_pic


#grayImage
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray_image", img);
histogram = cv.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(histogram, color='k')
# plt.show()
maxIntensity = np.where(histogram == np.amax(histogram))[0][0]


#Epsilon-Thresholding
# thresholding
gray_r = img.reshape(img.shape[0] * img.shape[1])
for i in range(gray_r.shape[0]):
    if abs(gray_r[i] - maxIntensity) <= epsilon:
        gray_r[i]=255
    else:
        gray_r[i]=0
img = gray_r.reshape(img.shape[0], img.shape[1])
t = img
cv.imshow('thresholding', t)



#edge detection
edges = cv.Laplacian(img, cv.CV_64F)
cv.imshow('Edge detection', edges)

# Overlay Extracted road image over original BnW image
overlay = cv.addWeighted(image_gray, 0.5, edges.astype(np.uint8), 0.5, 0)
cv.imshow('Overlay Image',overlay)


for i in range(len(outputs)):
    plt.subplot(1, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
