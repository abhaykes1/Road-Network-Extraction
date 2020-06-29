import numpy as np
import cv2 as cv

image = cv.imread('Original_BnW.png',0)

#This part is to apply simple linear transformation for brightness and contrast
# taking alpha and beta for adjusting contrast and brightness
# alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
# beta = int(input('* Enter the beta value [0-100]: '))

# new_image = np.zeros(image.shape, image.dtype)

# Doing the operation new_image(i,j) = alpha*image(i,j) + beta
# new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)

# non linear transformation,i.e, gamma correction

gamma = 2

lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv.LUT(image, lookUpTable)


cv.imshow('Original Image', image)
cv.imshow('New Image', res)
cv.waitKey(0)
cv.destroyAllWindows()

#saving the image after enhacment
#cv.imwrite('Enhanced_img.png',image)
