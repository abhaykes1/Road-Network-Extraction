import cv2 as cv
import matplotlib.pyplot as plt

imgpath = "./images/original.png"
img = cv.imread(imgpath, 1)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#gaussain filter
temp = img
for i in range(2):
    gaussian3 = temp
    gaussian3 = cv.GaussianBlur(gaussian3, (3, 3), 0)
    gaussian3 = cv.addWeighted(temp, 2, gaussian3, -1, 0)
    temp = gaussian3

#thresholding
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
gaussian3 = thresh

#edge detection
edges = cv.Canny(gaussian3,100,200)

cv.imshow('Original Image', img)
cv.imshow('New Image', edges)


#saving the image
cv.imwrite('Canny.png',edges)

#plotting
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()