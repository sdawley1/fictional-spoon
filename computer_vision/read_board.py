from operator import le
import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations


'''inputs are the picture of the board, dictionary of piece names (upper and lowercase for color)
and template filenames. does a for loop, calls another function that outputs the square each piece
is in. outputs 8x8 numpy array representing the current state.'''
def read_board(board_pic_path, template_names):
    os.chdir("./qrcodes")
    file_coords = {'a': 100, 'b': 200, 'c': 300, 'd': 400,
                    'e':500, 'f': 600, 'g': 700, 'h': 800}
    rank_coords = {1: 100, 2: 200, 3: 300, 4: 400,
                    5:500, 6: 600, 7: 700, 8: 800}

    for i in template_names:
        template = cv.imread(i,0)
        template = imutils.resize(template, width = int(img.shape[1] * 0.02))

        w, h = template.shape[::-1]
        method = eval('cv.TM_CCOEFF')
        res = cv.matchTemplate(board_pic_path,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
