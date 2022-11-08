/*

    Simple demo of THC Chess library

    This is a simple "hello world" exercise to get started with the THC chess library
    Just compile and link with thc.cpp. You only need thc.cpp and thc.h to use the
    THC library (see README.MD for more information)

 */

#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
#include <limits>
#include "thc.h"

void display_position( thc::ChessRules &cr, const std::string &description )
{
    std::string fen = cr.ForsythPublish();
    std::string s = cr.ToDebugStr();
    printf( "%s\n", description.c_str() );
    printf( "FEN (Forsyth Edwards Notation) = %s\n", fen.c_str() );
    printf( "Position = %s\n", s.c_str() );
}

int minimax(thc::ChessRules &cr, int depth, float alpha, float beta) {
    
    thc::TERMINAL terminal;
    cr.Evaluate(terminal);
    if(terminal == thc::TERMINAL_BCHECKMATE){
        return -1000;
    }
    else if(terminal == thc::TERMINAL_WCHECKMATE){
        return 1000;
    }
    else if(terminal == thc::TERMINAL_WSTALEMATE || terminal == thc::TERMINAL_BSTALEMATE){
        return 0;
    }
    else if(depth == 0){
        return 0;
    }
    
    
    if(cr.WhiteToPlay()){
        //maximizing player
    }
    else{
        //minimizing player
    }

    return 0;
}

thc::Move bestMove(thc::ChessRules &cr, int depth) {
    thc::Move mv;
    std::vector<thc::Move> moves;
    std::vector<bool> check;
    std::vector<bool> mate;
    std::vector<bool> stalemate;
    cr.GenLegalMoveList(moves, check, mate, stalemate);
    unsigned int len = moves.size();
    int alpha = -1000000;
    int beta = 1000000;
    if(cr.WhiteToPlay()){
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            int score = minimax(cr, depth-1, alpha, beta);
            cr.PopMove(moves[i]);
        }
    } 
    else {
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            int score = minimax(cr, depth-1, alpha, beta);
            cr.PopMove(moves[i]);
        }
    }
    return mv;
}

int main()
{
    // Example 1, Play a few good moves from the initial position
    thc::ChessRules cr;
    std::string input;

    display_position(cr, "Initial position");
    thc::TERMINAL terminal;
    cr.Evaluate(terminal);
    while(terminal == thc::NOT_TERMINAL){
        thc::Move mv = bestMove(cr, 3);
        cr.PushMove(mv);
        cr.Evaluate(terminal);

        std::cin >> input;
    }
}

