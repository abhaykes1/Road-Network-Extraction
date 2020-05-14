import numpy as np
import cv2 as cv

img = cv.imread('Road1.png',0)

#cv.imwrite('Original_BnW.png',img)

#display image
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()