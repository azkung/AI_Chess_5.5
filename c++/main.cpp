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

float boardCalc(thc::ChessRules &cr){
    std::string fen = cr.ForsythPublish();
    auto first_token = fen.substr(0, fen.find(' '));
    float score = 0.0;
    for(int i = 0; i < first_token.length(); i++){
        if(fen[i] == 'p'){
            score -= 1;
        }
        else if(fen[i] == 'P'){
            score += 1;
        }
        else if(fen[i] == 'n'){
            score -= 3;
        }
        else if(fen[i] == 'N'){
            score += 3;
        }
        else if(fen[i] == 'b'){
            score -= 3;
        }
        else if(fen[i] == 'B'){
            score += 3;
        }
        else if(fen[i] == 'r'){
            score -= 5;
        }
        else if(fen[i] == 'R'){
            score += 5;
        }
        else if(fen[i] == 'q'){
            score -= 9;
        }
        else if(fen[i] == 'Q'){
            score += 9;
        }
    }
    return score;
}

float minimax(thc::ChessRules &cr, int depth, float alpha, float beta) {
    
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
    
    float best = 0;
    
    if(cr.WhiteToPlay()){
        //maximizing player
        best = -100000;
        std::vector<thc::Move> moves;
        cr.GenLegalMoveList(moves);
        unsigned int len = moves.size();
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            float score = minimax(cr, depth - 1, alpha, beta);
            cr.PopMove(moves[i]); 
            best = std::max(best, score);
            alpha = std::max(alpha, best);
            if(beta <= alpha){
                break;
            }
        }
    }
    else{
        //minimizing player
        best = 100000;
        std::vector<thc::Move> moves;
        cr.GenLegalMoveList(moves);
        unsigned int len = moves.size();
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            float score = minimax(cr, depth - 1, alpha, beta);
            cr.PopMove(moves[i]); 
            best = std::min(best, score);
            beta = std::min(beta, best);
            if(beta <= alpha){
                break;
            }
        }
    }

    return best;
}

thc::Move bestMove(thc::ChessRules &cr, int depth) {
    thc::Move mv;
    std::vector<thc::Move> moves;
    cr.GenLegalMoveList(moves);
    unsigned int len = moves.size();
    float alpha = -1000000;
    float beta = 1000000;
    float best = 0;
    if(cr.WhiteToPlay()){
        best = -100000;
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            float score = minimax(cr, depth-1, alpha, beta);
            cr.PopMove(moves[i]);
            best = std::max(best, score);
            alpha = std::max(alpha, best);
            if(best == score){
                mv = moves[i];
            }
            if(beta <= alpha){
                break;
            }

        }
    } 
    else {
        best = 100000;
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            float score = minimax(cr, depth-1, alpha, beta);
            cr.PopMove(moves[i]);
            best = std::min(best, score);
            beta = std::min(beta, best);
            if(best == score){
                mv = moves[i];
            }
            if(beta <= alpha){
                break;
            }
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
        thc::Move mv = bestMove(cr, 6);
        cr.PushMove(mv);
        cr.Evaluate(terminal);

        display_position(cr, "After move");

        std::cin >> input;
    }
}

