from unittest import skip
import numpy as np
import chess
import chess.pgn
from numpy import save
import numpy



def boardToArray(board: chess.Board):
    for i in range(6):
        myboard = []
    
# def board_to_np(board):
#     pgn = board.epd()
#     foo = []
#     pieces = pgn.split(" ", 1)[0]
#     rows = pieces.split("/")
#     for i in range(6):
#         foo2 = []
#         for row in rows:
#             foo3 = []
#             for thing in row:
#                 if thing.isdigit():
#                     for x in range(0, int(thing)):
#                         foo3.append(0)
#                 else:
#                     if thing == 'P' and i == 0:
#                         foo3.append(1)
#                     elif thing == 'p' and i == 0:
#                         foo3.append(-1)
#                     elif thing == 'N' and i == 1:
#                         foo3.append(1)
#                     elif thing == 'n' and i == 1:
#                         foo3.append(-1)
#                     elif thing == 'B' and i == 2:
#                         foo3.append(1)
#                     elif thing == 'b' and i == 2:
#                         foo3.append(-1)
#                     elif thing == 'R' and i == 3:
#                         foo3.append(1)
#                     elif thing == 'r' and i == 3:
#                         foo3.append(-1)
#                     elif thing == 'Q' and i == 4:
#                         foo3.append(1)
#                     elif thing == 'q' and i == 4:
#                         foo3.append(-1)
#                     elif thing == 'K' and i == 5:
#                         foo3.append(1)
#                     elif thing == 'k' and i == 5:
#                         foo3.append(-1)
#                     else:
#                         foo3.append(0)
#             foo2.append(foo3)
#         foo.append(foo2)
#     return np.array(foo)

def board_to_np(board: chess.Board):
    arr = np.zeros((6,8,8))
    row = 7
    col = 0
    for square in chess.SQUARES:
        thing = board.piece_at(square) 
        if(thing):
            if(thing.symbol() == 'P'):
                arr[0][row][col] = 1
            elif(thing.symbol() == 'p'):
                arr[0][row][col] = -1
            elif(thing.symbol() == 'N'):
                arr[1][row][col] = 1
            elif(thing.symbol() == 'n'):
                arr[1][row][col] = -1
            elif(thing.symbol() == 'B'):
                arr[2][row][col] = 1
            elif(thing.symbol() == 'b'):
                arr[2][row][col] = -1
            elif(thing.symbol() == 'R'):
                arr[3][row][col] = 1
            elif(thing.symbol() == 'r'):
                arr[3][row][col] = -1
            elif(thing.symbol() == 'Q'):
                arr[4][row][col] = 1
            elif(thing.symbol() == 'q'):
                arr[4][row][col] = -1
            elif(thing.symbol() == 'K'):
                arr[5][row][col] = 1
            elif(thing.symbol() == 'k'):
                arr[5][row][col] = -1
        col += 1
        if col > 7:
            col = 0
            row -=1
    return arr

# def move_to_np(move: chess.Move):
#     arr = np.zeros((8,8))
#     square = move.from_square
#     col = square % 8
#     row = 7 - int(square/8)
#     return row*8 + col

'''
SQUARES = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8,
] = range(64)
'''

def square_to_row_col(square : int):
    return chess.SQUARE_NAMES[square]

def format(path : str, idx : int, total_games : int, skip_ties : bool = False, minElo : int = 2500, turn = True):
    with open("datasets/ficsgamesdb_2021_standard2000_nomovetimes_264388.pgn") as pgn:
        x = []
        y = []
        for i in range(idx):
            game = chess.pgn.read_game(pgn)
        for i in range(total_games):
            game = chess.pgn.read_game(pgn)
            result = game.headers["Result"]
            plyCount = game.headers["PlyCount"]
            if(int(plyCount) < 30):
                continue
            if(int(game.headers["WhiteElo"]) < minElo):
                continue

            board = game.board()
            for move in game.mainline_moves():
                if(board.turn == turn):
                    x.append(board_to_np(board))
                    y.append(move.from_square)
                board.push(move)

        x = np.array(x)
        y = np.array(y)
        print(x.shape)
        print(y.shape)
        save(path + "_x.npy", x)
        save(path + "_y.npy", y)