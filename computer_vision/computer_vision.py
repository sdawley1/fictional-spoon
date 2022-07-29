import sys
from operator import le
import cv2 as cv
import imutils
import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations
sys.path.append('../')
from pathfinding.create_random_fen import fen_from_board

def get_square(top_left: tuple, bottom_right: tuple) -> tuple:
    '''
    returns the square corresponding to a piece's pixel location in the board image
    :param top_left: tuple of the pixel coords of the top left of the qr code
    :param bottom_right: tuple of the pixel coords of the bottom right of the qr code
    '''

    file_coords_tl = {i: 105*(i-1)+20 for i in range(1, 9)}
    rank_coords_tl = {9-i: 103*(i-1)+10 for i in range(1, 9)}

    file_coords_br = {i: 105*(i)+20 for i in range(1, 9)}
    rank_coords_br = {9-i: 103*(i)+10 for i in range(1, 9)}

    file_coords_avg = {i: np.mean([file_coords_tl[i], file_coords_br[i]]) for i in range(1, 9)}
    rank_coords_avg = {i: np.mean([rank_coords_tl[i], rank_coords_br[i]]) for i in range(1, 9)}

    file_num = {1: 'a', 2:'b', 3: 'c', 4: 'd',
                    5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    
    file_coord_tl = top_left[0]
    rank_coord_tl = top_left[1]

    file_coord_br = bottom_right[0]
    rank_coord_br = bottom_right[1]

    file_coord_avg = np.mean([file_coord_tl, file_coord_br])
    rank_coord_avg = np.mean([rank_coord_tl, rank_coord_br])

    file, _ = min(file_coords_avg.items(), key=lambda x: abs(file_coord_avg - x[1]))
    rank, _ = min(rank_coords_avg.items(), key=lambda x: abs(rank_coord_avg - x[1]))

    return(file, rank)


def read_board(board_pic_path: str, template_fnames: list, piece_names: list) -> str:
    '''
    returns a fen string of the current state of the board
    :param board_pic_path: pathname to newest board picture
    :param template_fnames: list of qr code filepaths as strings
    :param piece_names: list of piece names, in same order as corresponding qr codes    
    '''
    board = np.empty((8, 8), dtype='str')
    board[:] = ' '

    for qrcode, piece in zip(template_fnames, piece_names):
        img = cv.imread(board_pic_path,0)

        template = cv.imread(qrcode,0)
        template = imutils.resize(template, width = int(img.shape[1] * 0.05))
        w, h = template.shape[::-1]

        method = eval('cv.TM_CCOEFF')
        res = cv.matchTemplate(img,template,method)
        _, _, _, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
     
        file, rank =  get_square(top_left, bottom_right)
        board[8-rank][file-1] = piece
    return(fen_from_board(board))

#print(read_board('cvtest2.png', ['qrcodes/empty.jpg', 'qrcodes/12345.jpg', 'qrcodes/1234.jpg'], ['K', 'k', 'N']))


def check_update(current_board: str, board_pic_path: str, template_fnames: list, piece_names: list) -> bool:
    '''
    check if the board has changed from its previous state
    :param current_board: fen string of the board's current position
    :param board_pic_path: pathname to newest board picture
    :param template_fnames: list of qr code filepaths as strings
    :param piece_names: list of piece names, in same order as corresponding qr codes
    '''
    board_updated = False
    next_board = read_board(board_pic_path, template_fnames, piece_names)

    if current_board != next_board:
        board_updated = True

    return board_updated