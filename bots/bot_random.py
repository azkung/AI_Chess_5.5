import chess
import random

def bestMove(board: chess.Board):
    moves = board.legal_moves
    count = 0
    for move in moves:
        count += 1

    choice = random.randint(0,count-1)
    for idx, move in enumerate(moves):
        if(idx == choice):
            return move
    
    