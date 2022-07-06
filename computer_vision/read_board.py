import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('qrcodes/sampleqr.jpg',0)
template = cv.imread('qrcodes/1345.jpg',0)
plt.imshow(template)
plt.show()
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = 'cv.TM_CCOEFF'

method = eval(methods)
# Apply template Matching
res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img,top_left, bottom_right, (255, 0, 0), 2)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)

#plt.imshow(resized)
plt.show()
