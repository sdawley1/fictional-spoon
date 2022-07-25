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
    #file_coords = {'a': 61, 'b': 130, 'c': 199, 'd': 268,
    #                'e': 337, 'f': 406, 'g': 475, 'h': 544}
    #rank_coords = {9-i: 70*(i-1) + 48 for i in range(1, 9)}
    file_coords = {i: 105*(i-1)+20 for i in range(1, 9)}
    rank_coords = {9-i: 103*(i-1)+10 for i in range(1, 9)}

    file_num = {1: 'a', 2:'b', 3: 'c', 4: 'd',
                    5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    
    #file_coord = round(top_left[0], -1)
    #rank_coord = round(top_left[1], -1)
    file_coord = top_left[0]
    rank_coord = top_left[1]

    file, _ = min(file_coords.items(), key=lambda x: abs(file_coord - x[1]))
    rank, _ = min(rank_coords.items(), key=lambda x: abs(rank_coord - x[1]))
    print(str(file_num[file])+str(rank))

    return(file, rank)

'''inputs are the picture of the board, dictionary of piece names (upper and lowercase for color)
and template filenames. does a for loop, calls another function that outputs the square each piece
is in. outputs 8x8 numpy array representing the current state.'''
def read_board(board_pic_path, template_fnames, piece_names):
    board = np.empty((8, 8), dtype='str')
    board[:] = ' '

    for qrcode, piece in zip(template_fnames, piece_names):
        img = cv.imread(board_pic_path,0)

        template = cv.imread(qrcode,0)
        template = imutils.resize(template, width = int(img.shape[1] * 0.05))
        method = eval('cv.TM_CCOEFF')
        res = cv.matchTemplate(img,template,method)
        _, _, _, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        print(top_left, piece)
        
        file, rank =  get_square(top_left)
        board[8-rank][file-1] = piece
    #return(board)
    return(fen_from_board(board))

print(read_board('cvtest2.png', ['qrcodes/empty.jpg', 'qrcodes/12345.jpg', 'qrcodes/1234.jpg'],
                    ['K', 'k', 'N']))