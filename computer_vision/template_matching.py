from operator import le
import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations

letters = '12345'
strings = []
templates = []

for i in [1, 2, 3, 4, 5]:
    strings += list(combinations(letters, i))

for j in strings:
    templates.append(''.join(j))
templates = [i+'.jpg' for i in templates]

img = cv.imread('qrcodes/allcodes.png',0)

template = cv.imread('qrcodes/123.jpg',0)
template = imutils.resize(template, width = int(img.shape[1] * 0.02))

w, h = template.shape[::-1]

method = eval('cv.TM_CCOEFF')
# Apply template Matching
res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img,top_left, bottom_right, (255, 0, 255), 2)
plt.subplot(121),plt.imshow(res,cmap = 'viridis')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'viridis')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

plt.show()