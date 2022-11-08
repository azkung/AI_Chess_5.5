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


def AI(board : chess.Board, depth, alpha, beta, inf_depth):
    #Minimax AI that beats you
    #White maximizing, Black minimizing
    global positions
    positions += 1
    
    outcome = board.outcome()
    if outcome != None:
        if(outcome.winner == True):
            return float('inf'), None
        elif(outcome.winner == False):
            return float('-inf'), None
        else:
            if(board.turn == True):
                return float('-inf'), None
            else:
                return float('inf'), None
        

    if depth == 0:
        return scoreCalcBoard(board), None

    if board.turn == True:
        #Maximizing White
        maxScore = float('-inf')
        maxMove = None
        legal_moves = list(board.legal_moves)
        sorted_legal_moves = legal_moves

        if(depth >= inf_depth):
            x = tools.board_to_np(board)
            x = torch.Tensor(x)
            y = whiteNet(x.unsqueeze(0))
            y = torch.argsort(y, descending=True)
            en = enumerate(y[0])
            d_old = dict(en)
            d = dict((v.item(),k) for k,v in d_old.items())
            sorted_legal_moves = sorted(legal_moves, key=lambda x: d[x.from_square]) 

        
        for move in sorted_legal_moves:
            board.push(move)
            score = AI(board, depth-1, alpha, beta, inf_depth)[0]
            board.pop()
            
            previousMaxScore = maxScore
            maxScore = max(score, maxScore)

            if maxScore != previousMaxScore:
                maxMove = move
                
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        return maxScore, maxMove

    else:
        #Minimizing Black
        minScore = float('inf')
        minMove = None
        legal_moves = list(board.legal_moves)
        sorted_legal_moves = legal_moves

        if(depth >= inf_depth):
            x = tools.board_to_np(board)
            x = torch.Tensor(x)
            y = blackNet(x.unsqueeze(0))
            y = torch.argsort(y, descending=True)
            en = enumerate(y[0])
            d_old = dict(en)
            d = dict((v.item(),k) for k,v in d_old.items())
            sorted_legal_moves = sorted(legal_moves, key=lambda x: d[x.from_square])


        for move in sorted_legal_moves:
            board.push(move)
            score = AI(board, depth-1, alpha, beta, inf_depth)[0]
            board.pop()
            
            previousMinScore = minScore
            minScore = min(score, minScore)

            if minScore != previousMinScore:
                minMove = move 
            
            beta = min(beta, score)

            if beta <= alpha:
                break

        return minScore, minMove
    

def bestMove(board: chess.Board):
    global positions
    positions = 0
    score, bestMove = AI(board, 5, float('-inf'), float('inf'), 3)
    print(positions)
    if bestMove == None:
        for move in board.legal_moves:
            return move
    return bestMove
