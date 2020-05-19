import cv2
import matplotlib.pyplot as plt

imgpath = "./images/original.png"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

temp = img
for i in range(2):
    gaussian3 = temp
    gaussian3 = cv2.GaussianBlur(gaussian3, (3, 3), 0)
    gaussian3 = cv2.addWeighted(temp, 2, gaussian3, -1, 0)
    temp = gaussian3

temp = img
for i in range(4):
    gaussian7 = temp
    gaussian7 = cv2.GaussianBlur(gaussian7, (7, 7), 0)
    gaussian7 = cv2.addWeighted(temp, 2, gaussian7, -1, 0)
    temp = gaussian7

temp = img
for i in range(3):
    gaussian9 = temp
    gaussian9 = cv2.GaussianBlur(gaussian9, (9, 9), 0)
    gaussian9 = cv2.addWeighted(temp, 2, gaussian9, -1, 0)
    temp = gaussian9

titles = ['Original Image', '3*3 and 2 times',
          '7*7 and 4 times', '9*9 and 3 times']

outputs = [img, gaussian3, gaussian7, gaussian9]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()