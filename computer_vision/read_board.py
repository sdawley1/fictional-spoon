from operator import le
import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations

'''inputs are the picture of the board, dictionary of piece names (upper and lowercase for color)
and template names. does a for loop, calls another function that outputs the square each piece
is in. outputs 8x8 numpy array representing the current state.'''
def read_board(board_pic, template_names):
    os.chdir("./qrcodes")
    ranks = {}

    for i in template_names:
        template = cv.imread(i,0)
        template = imutils.resize(template, width = int(img.shape[1] * 0.02))

        w, h = template.shape[::-1]
        method = eval('cv.TM_CCOEFF')
        res = cv.matchTemplate(board_pic,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
