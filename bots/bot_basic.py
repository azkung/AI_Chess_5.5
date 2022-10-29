import chess
import math

        
def scoreCalcBasic(board: chess.Board):
    currentScore = 0

    for i in range(1,7):
        if i == 1:
            currentScore += len(board.pieces(i, chess.COLORS[0]))
        if i == 2:
            currentScore += 3*len(board.pieces(i, chess.COLORS[0]))
        if i == 3:
            currentScore += 3*len(board.pieces(i, chess.COLORS[0]))
        if i == 4:
            currentScore += 5*len(board.pieces(i, chess.COLORS[0]))
        if i == 5:
            currentScore += 9*len(board.pieces(i, chess.COLORS[0]))
            
    for i in range(1,7):
        if i == 1:
            currentScore -= len(board.pieces(i, chess.COLORS[1]))
        if i == 2:
            currentScore -= 3*len(board.pieces(i, chess.COLORS[1]))
        if i == 3:
            currentScore -= 3*len(board.pieces(i, chess.COLORS[1]))
        if i == 4:
            currentScore -= 5*len(board.pieces(i, chess.COLORS[1]))
        if i == 5:
            currentScore -= 9*len(board.pieces(i, chess.COLORS[1]))
    
    return currentScore

def scoreCalcBoard(board):
    return scoreCalcBasic(board)


def AI(board : chess.Board, depth, alpha, beta):
    #Minimax AI that beats you
    #White maximizing, Black minimizing
    
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
    score, bestMove = AI(board, 5, float('-inf'), float('inf'))
    if bestMove == None:
        for move in board.legal_moves:
            return move
    return bestMove