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

#edge detection
edges = cv.Canny(gaussian3,100,200)

cv.imshow('Original Image', img)
cv.imshow('New Image', edges)
cv.waitKey(0)
cv.destroyAllWindows()

#saving the image
cv.imwrite('Canny.png',edges)

#plotting
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()