#include "board.h"

#include <iostream>

/*
- = black
0 = empty
+ = white
1 = pawn
2 = knight
3 = bishop
4 = rook
5 = queen
6 = king
*/

Board::Board() {
    turn = true;
    for (int i = 0; i < 64; i++) {
        board[i] = 0;
    }
    board[0] = 4;
    board[1] = 2;
    board[2] = 3;
    board[3] = 5;
    board[4] = 6;
    board[5] = 3;
    board[6] = 2;
    board[7] = 4;
    board[8] = 1;
    board[9] = 1;
    board[10] = 1;
    board[11] = 1;
    board[12] = 1;
    board[13] = 1;
    board[14] = 1;
    board[15] = 1;
    board[48] = -1;
    board[49] = -1;
    board[50] = -1;
    board[51] = -1;
    board[52] = -1;
    board[53] = -1;
    board[54] = -1;
    board[55] = -1;
    board[56] = -4;
    board[57] = -2;
    board[58] = -3;
    board[59] = -5;
    board[60] = -6;
    board[61] = -3;
    board[62] = -2;
    board[63] = -4;
}

Board::~Board() {}

void Board::printBoard() {
    int alp = 0;
    int num = 7;
    for (int i = 0; i < 64; i++) {
        if(alp == 8){
            alp = 0;
            num--;
            std::cout << std::endl;
        }
        int idx = (num * 8) + alp;
        switch (board[idx]) {
            case 0:
                std::cout << ". ";
                break;
            case 1:
                std::cout << "P ";
                break;
            case 2:
                std::cout << "N ";
                break;
            case 3:
                std::cout << "B ";
                break;
            case 4:
                std::cout << "R ";
                break;
            case 5:
                std::cout << "Q ";
                break;
            case 6:
                std::cout << "K ";
                break;
            case -1:
                std::cout << "p ";
                break;
            case -2:
                std::cout << "n ";
                break;
            case -3:
                std::cout << "b ";
                break;
            case -4:
                std::cout << "r ";
                break;
            case -5:
                std::cout << "q ";
                break;
            case -6:
                std::cout << "k ";
                break;
        }
        ++alp;
    }
    std::cout << std::endl;
}