import bots.bot_attack as bot_attack
import bots.bot_basic as bot_basic
# import bots.bot_inference as bot_inference
import bots.bot_middle as bot_middle
import bots.bot_random as bot_random
import chess
import pygame
import time

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 800,800
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('AI Chess')

WHITE = (255,255,255)
DARKGREEN = (119, 149, 86)
LIGHTGREEN = (235, 236, 208)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
SILVER = (192,192,192)
DARKGREY = 	(100,100,100)
BEIGE = (217,179,130)
DARKERGREEN = (1,49,31)

DARKSQUARE = DARKGREEN
LIGHTSQUARE = LIGHTGREEN

whitePawn = pygame.image.load('images/white-pawn.png')
whiteRook = pygame.image.load('images/white-rook.png')
whiteKnight = pygame.image.load('images/white-knight.png')
whiteBishop = pygame.image.load('images/white-bishop.png')
whiteQueen = pygame.image.load('images/white-queen.png')
whiteKing = pygame.image.load('images/white-king.png')

blackBishop = pygame.image.load('images/black-bishop.png')
blackKing = pygame.image.load('images/black-king.png')
blackKnight = pygame.image.load('images/black-knight.png')
blackPawn = pygame.image.load('images/black-pawn.png')
blackQueen = pygame.image.load('images/black-queen.png')
blackRook = pygame.image.load('images/black-rook.png')

whitePawn = pygame.transform.scale(whitePawn, (100, 100))
whiteRook = pygame.transform.scale(whiteRook, (100, 100))
whiteKnight = pygame.transform.scale(whiteKnight, (100, 100))
whiteBishop = pygame.transform.scale(whiteBishop, (100, 100))
whiteQueen = pygame.transform.scale(whiteQueen, (100, 100))
whiteKing = pygame.transform.scale(whiteKing, (100, 100))

blackPawn = pygame.transform.scale(blackPawn, (100, 100))
blackRook = pygame.transform.scale(blackRook, (100, 100))
blackKnight = pygame.transform.scale(blackKnight, (100, 100))
blackBishop = pygame.transform.scale(blackBishop, (100, 100))
blackQueen = pygame.transform.scale(blackQueen, (100, 100))
blackKing = pygame.transform.scale(blackKing, (100, 100))

def pieceDraw(name, x, y):
    if name == -1:
        screen.blit(blackPawn, (x*100,y*100))
    elif name == -6:
        screen.blit(blackKing, (x*100,y*100))
    elif name == -5:
        screen.blit(blackQueen, (x*100,y*100))
    elif name == -4:
        screen.blit(blackRook, (x*100,y*100))
    elif name == -2:
        screen.blit(blackKnight, (x*100,y*100))
    elif name == -3:
        screen.blit(blackBishop, (x*100,y*100))
    
    elif name == 1:
        screen.blit(whitePawn, (x*100,y*100))
    elif name == 6:
        screen.blit(whiteKing, (x*100,y*100))
    elif name == 5:
        screen.blit(whiteQueen, (x*100,y*100))
    elif name == 4:
        screen.blit(whiteRook, (x*100,y*100))
    elif name == 2:
        screen.blit(whiteKnight, (x*100,y*100))
    elif name == 3:
        screen.blit(whiteBishop, (x*100,y*100))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

board = chess.Board()

screen.fill((0, 0, 0))
for i in range(0,8,2):
    for j in range(0,8,2):
        pygame.draw.rect(screen, LIGHTSQUARE, (i*100,j*100,100,100))
for i in range(1,9,2):
    for j in range(1,9,2):
        pygame.draw.rect(screen, LIGHTSQUARE, (i*100,j*100,100,100))

for i in range(0,8,2):
    for j in range(0,8,2):
        pygame.draw.rect(screen, DARKSQUARE, (i*100+100,j*100,100,100))
for i in range(1,9,2):
    for j in range(1,9,2):
        pygame.draw.rect(screen, DARKSQUARE, (i*100-100,j*100,100,100))

s = 0
for square in chess.SQUARES:
    piece = board.piece_at(square)
    x = s%8
    y = int(s/8)
    if piece != None:
        if piece.piece_type == 1:
            if piece.color == True:
                pieceDraw(1, x, y)
            else:
                pieceDraw(-1, x, y)
                
        if piece.piece_type == 2:
            if piece.color == True:
                pieceDraw(2, x, y)
            else:
                pieceDraw(-2, x, y)
                
        if piece.piece_type == 3:
            if piece.color == True:
                pieceDraw(3, x, y)
            else:
                pieceDraw(-3, x, y)
                
        if piece.piece_type == 4:
            if piece.color == True:
                pieceDraw(4, x, y)
            else:
                pieceDraw(-4, x, y)
        
        if piece.piece_type == 5:
            if piece.color == True:
                pieceDraw(5, x, y)
            else:
                pieceDraw(-5, x, y)

        if piece.piece_type == 6:
            if piece.color == True:
                pieceDraw(6, x, y)
            else:
                pieceDraw(-6, x, y)
    s += 1
pygame.display.flip()
input()

moves = 0
while board.is_game_over() == False:
    screen.fill((0, 0, 0))
    for i in range(0,8,2):
        for j in range(0,8,2):
            pygame.draw.rect(screen, LIGHTSQUARE, (i*100,j*100,100,100))
    for i in range(1,9,2):
        for j in range(1,9,2):
            pygame.draw.rect(screen, LIGHTSQUARE, (i*100,j*100,100,100))

    for i in range(0,8,2):
        for j in range(0,8,2):
            pygame.draw.rect(screen, DARKSQUARE, (i*100+100,j*100,100,100))
    for i in range(1,9,2):
        for j in range(1,9,2):
            pygame.draw.rect(screen, DARKSQUARE, (i*100-100,j*100,100,100))

    s = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        x = s%8
        y = int(s/8)
        if piece != None:
            if piece.piece_type == 1:
                if piece.color == True:
                    pieceDraw(1, x, y)
                else:
                    pieceDraw(-1, x, y)
                    
            if piece.piece_type == 2:
                if piece.color == True:
                    pieceDraw(2, x, y)
                else:
                    pieceDraw(-2, x, y)
                    
            if piece.piece_type == 3:
                if piece.color == True:
                    pieceDraw(3, x, y)
                else:
                    pieceDraw(-3, x, y)
                    
            if piece.piece_type == 4:
                if piece.color == True:
                    pieceDraw(4, x, y)
                else:
                    pieceDraw(-4, x, y)
            
            if piece.piece_type == 5:
                if piece.color == True:
                    pieceDraw(5, x, y)
                else:
                    pieceDraw(-5, x, y)

            if piece.piece_type == 6:
                if piece.color == True:
                    pieceDraw(6, x, y)
                else:
                    pieceDraw(-6, x, y)
        s += 1

    if board.turn:
        bestMove = bot_middle.bestMove(board)
        board.push(bestMove)
    else:
        bestMove = bot_middle.bestMove(board)
        board.push(bestMove)

    if(board.is_game_over()):
        break
    

    time.sleep(3)
    pygame.display.flip()

text = pygame.font.SysFont("arial",50,bold=True)
if(board.turn):
    TextSurf, TextRect = text_objects("CHECKMATE BLACK WINS", text, DARKGREY)
    TextRect.center = (400,350)
    screen.blit(TextSurf, TextRect)
else:
    TextSurf, TextRect = text_objects("CHECKMATE WHITE WINS", text, DARKGREY)
    TextRect.center = (400,350)
    screen.blit(TextSurf, TextRect)