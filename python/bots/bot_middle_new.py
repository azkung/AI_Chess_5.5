import chess
import math

global positions

def scoreCalcMiddleRush(board: chess.Board):
    currentScore = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        
        if piece != None:
            c = square%8
            r = math.floor(square/8)
            distanceFromCenter = math.sqrt(((c-3.5)**2) + ((r-3.5)**2))
            
            if piece.piece_type == 1:
                if piece.color == True:
                    currentScore += (4 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (4 +  ((6-round(distanceFromCenter))/30))
                    
            if piece.piece_type == 2:
                if piece.color == True:
                    currentScore += (12 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (12 +  ((6-round(distanceFromCenter))/30))
                    
            if piece.piece_type == 3:
                if piece.color == True:
                    currentScore += (12 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (12 +  ((6-round(distanceFromCenter))/30))
                    
            if piece.piece_type == 4:
                if piece.color == True:
                    currentScore += (20 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (20 +  ((6-round(distanceFromCenter))/30))
            
            if piece.piece_type == 5:
                if piece.color == True:
                    currentScore += (32 +  ((6-round(distanceFromCenter))/30))
                else:
                    currentScore -= (32 +  ((6-round(distanceFromCenter))/30))
                    
    return currentScore


def scoreCalcBoard(board):
    return scoreCalcMiddleRush(board)


def AI(board : chess.Board, depth, alpha, beta):
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
    global positions
    positions = 0
    score, bestMove = AI(board, 6, float('-inf'), float('inf'))
    print(positions)
    if bestMove == None:
        for move in board.legal_moves:
            return move
    return bestMove