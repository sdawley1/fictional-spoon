from operator import le
import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations

#file_coords = {1: 51, 2: 122, 3: 199, 4: 268,
#                5: 337, 6: 406, 7: 480, 8: 549}
#rank_coords = {9-i: 70*(i-1) + 48 for i in range(1, 9)}

file_coords = {i: 105*(i-1)+20 for i in range(1, 9)}
rank_coords = {9-i: 103*(i-1)+10 for i in range(1, 9)}
print(file_coords)
print(rank_coords)

img=cv.imread('cvtest2.png')
for i in range(1, 8):
    cv.rectangle(img, (file_coords[i], rank_coords[i]),
        (file_coords[i+1], rank_coords[i+1]), (255, 0, 255), 2)
#cv.rectangle(img, (file_coords[5], rank_coords[5]), (file_coords[5]+1, rank_coords[5]+5), (255, 0, 255), 2)
#cv.rectangle(img, (20, 4), (120, 106), (255, 0, 255), 2)
cv.imshow('img', img)
cv.waitKey(0)