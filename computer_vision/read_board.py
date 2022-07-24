import sys
from operator import le
import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations
sys.path.append('../')
from pathfinding.create_random_fen import fen_from_board

def get_square(top_left):
    file_coords = {'a': 100, 'b': 200, 'c': 300, 'd': 400,
                    'e':500, 'f': 600, 'g': 700, 'h': 800}
    rank_coords = {1: 100, 2: 200, 3: 300, 4: 400,
                    5:500, 6: 600, 7: 700, 8: 800}
    file_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
                    'e':5, 'f': 6, 'g': 7, 'h': 8}
    
    file_coord = round(top_left[0], -1)
    rank_coord = round(top_left[1], -1)

    file, _ = min(file_coords.items(), key=lambda x: abs(file_coord - x[1]))
    rank, _ = min(rank_coords.items(), key=lambda x: abs(rank_coord - x[1]))

    return(file_num[file], rank)

'''inputs are the picture of the board, dictionary of piece names (upper and lowercase for color)
and template filenames. does a for loop, calls another function that outputs the square each piece
is in. outputs 8x8 numpy array representing the current state.'''
def read_board(board_pic_path, template_fnames, piece_names):
    board = np.empty((8, 8), dtype='str')
    board[:] = ' '

    for qrcode, piece in zip(template_fnames, piece_names):
        board_pic = cv.imread(board_pic_path)
        template = cv.imread(qrcode,0)
        template = imutils.resize(template, width = int(board_pic.shape[1] * 0.02))

        w, h = template.shape[::-1]
        method = eval('cv.TM_CCOEFF')
        res = cv.matchTemplate(board_pic_path,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc

        file, rank =  get_square(top_left)
        board[file-1][rank-1] = piece
    
    return(fen_from_board(board))

print(round(131, -1))