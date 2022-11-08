import bots.bot_attack as bot_attack
import bots.bot_basic as bot_basic
import bots.bot_middle as bot_middle
import bots.bot_middle_new as bot_middle_new
import bots.bot_random as bot_random
import bots.bot_net_traversal as bot_net_traversal
import bots.bot_net_traversal_2 as bot_net_traversal_2
import bots.bot_custom as bot_custom
import chess
import time

board = chess.Board()

    
print(board)
print()
moves = 0
while board.is_game_over() == False:
    print("-------------------------")
    print(board.turn)
    s = time.perf_counter()
    bestMove = bot_custom.bestMove(board)
    e = time.perf_counter()
    print(bestMove)
    print(round(e-s,4))
    board.push(bestMove)
    print(board)
    # print(board.fen)
    print()

    if(board.is_game_over()):
        break

    print(board.turn)

    print(board.legal_moves)
    
    # s = time.perf_counter()
    # bestMove = bot_attack.bestMove(board)
    # e = time.perf_counter()
    # print(round(e-s,4))
    # board.push(bestMove)
    # print(board)
    # # print(board.fen)
    # print()


    bestMove = input("Enter Move \n")
    board.push_san(bestMove)
    print(board)
    # print(board.fen)
    print()

    moves += 1

    
print(board)
print(moves)
print(board.outcome())
if(board.outcome().winner == True):
    print("White Wins")
elif(board.outcome().winner == False):
    print("Black Wins")
else:
    print("Draw")
