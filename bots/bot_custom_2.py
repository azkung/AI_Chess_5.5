from string import whitespace
import chess
import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
from training.model import Net
import os.path
import tools
import math
import multiprocessing

global positions

WHITE_MODEL_PATH = os.path.dirname(__file__) + '/../models/WhitePieceSelector'
BLACK_MODEL_PATH = os.path.dirname(__file__) + '/../models/BlackPieceSelector'
whiteNet = Net()
blackNet = Net()

whiteNet.load_state_dict(torch.load(WHITE_MODEL_PATH))
blackNet.load_state_dict(torch.load(BLACK_MODEL_PATH))


def scoreCalcCustom(board: chess.Board):
    currentScore = 0
    col = 0
    row = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        whiteRook1 = None
        blackRook1 = None

        if piece != None:
            distanceFromCenter = ((col-3.5)**2) + ((row-3.5)**2)**0.5
            inverseDistanceFromCenter = 6 - distanceFromCenter
            inverseDistanceFromCenter = inverseDistanceFromCenter/30
            if piece.piece_type == 1:
                if piece.color == True:
                    currentScore += 4
                    currentScore += inverseDistanceFromCenter*2
                else:
                    currentScore -= 4
                    currentScore -= inverseDistanceFromCenter*2
                    
            elif piece.piece_type == 2:
                if piece.color == True:
                    currentScore += 12
                    currentScore += inverseDistanceFromCenter*2
                else:
                    currentScore -= 12
                    currentScore -= inverseDistanceFromCenter*2
                    
            elif piece.piece_type == 3:
                if piece.color == True:
                    currentScore += 12
                    currentScore += inverseDistanceFromCenter
                else:
                    currentScore -= 12
                    currentScore -= inverseDistanceFromCenter
                    
            elif piece.piece_type == 4:
                if piece.color == True:
                    if(whiteRook1 == None):
                        whiteRook1 = square
                    else:
                        if(whiteRook1 in board.attacks(square)):
                            currentScore += 7
                    currentScore += 20
                    currentScore += inverseDistanceFromCenter
                else:
                    if(blackRook1 == None):
                        blackRook1 = square
                    else:
                        if(blackRook1 in board.attacks(square)):
                            currentScore -= 7
                    currentScore -= 20
                    currentScore -= inverseDistanceFromCenter
                    
            
            elif piece.piece_type == 5:
                if piece.color == True:
                    currentScore += 32
                    currentScore += inverseDistanceFromCenter
                else:
                    currentScore -= 32
                    currentScore -= inverseDistanceFromCenter
        else:
            if row == 0:
                currentScore += 0.4
            elif row == 7:
                currentScore -= 0.4
    
        col += 1
        if(col >= 8):
            row += 1
            col = 0

    return currentScore


def scoreCalcBoard(board):
    return scoreCalcCustom(board)

    

def bestMove(board: chess.Board):
    global positions
    positions = 0

    depth = 5
    alpha = -math.inf
    beta = math.inf
    bestMove = None
    bestScore = -math.inf
    while True:
        if depth == 0:
            depth += 1
        
        
