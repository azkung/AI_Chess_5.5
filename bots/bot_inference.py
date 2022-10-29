import chess
import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
import time
from training.model import Net
import os.path
import tools

MODEL_PATH = os.path.dirname(__file__) + '/../models/1666163225'
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = Net()
net.load_state_dict(torch.load(MODEL_PATH))

def boardToTensor(board: chess.Board):
    inputArray = tools.board_to_np(board)
    inputTensor = torch.Tensor(inputArray)
    inputTensor = inputTensor[None]
    return inputTensor

def scoreCalcBoard(board : chess.Board):
    with torch.no_grad():
        score = net(boardToTensor(board))
        return score.item()
        
def AI(board : chess.Board, depth, alpha, beta):
    #Minimax AI that beats you
    #White maximizing, Black minimizing
    
    if board.is_checkmate():
        if board.turn == True:
            return float('-inf'), None
        else:
            return float('inf'), None
    
    if board.is_stalemate():
        return 0, None
    
    if board.is_game_over():
        return 0, None
        

    if depth == 0:
        return scoreCalcBoard(board), None

    if board.turn == True:
        #Maximizing White
        maxScore = float('-inf')
        maxMove = None
        
        for move in board.legal_moves:
            board.push(move)
            score = AI(board, depth-1, alpha, beta)[0]
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
        
        for move in board.legal_moves:
            board.push(move)
            score = AI(board, depth-1, alpha, beta)[0]
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
    score, bestMove = AI(board, 3, float('-inf'), float('inf'))
    print(score)
    if bestMove == None:
        for move in board.legal_moves:
            return move
    return bestMove

    
# def bestMove(board: chess.Board):
#     highestScore = -100
#     lowestScore = 100
    
#     for move in board.legal_moves:
#         board.push(move)
#         with torch.no_grad():
#             score = scoreCalcBoard(board)
#             print(move, ": ", score)
#             if score > highestScore:
#                 highestScore = score
#                 highestScoreMove = move
#             if score < lowestScore:
#                 lowestScore = score
#                 lowestScoreMove = move
#         board.pop()
#     if(board.turn):
#         return highestScoreMove
#     else:
#         return lowestScoreMove
