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
#include <math.h>
#include "thc.h"

int pos = 0;
std::string m = "";
std::string m2 = "";

void display_position( thc::ChessRules &cr, const std::string &description )
{
    std::string fen = cr.ForsythPublish();
    std::string s = cr.ToDebugStr();
    printf( "%s\n", description.c_str() );
    printf( "FEN (Forsyth Edwards Notation) = %s\n", fen.c_str() );
    printf( "Position = %s\n", s.c_str() );
}

float basicCalc(thc::ChessRules &cr){
    std::string fen = cr.ForsythPublish();
    auto first_token = fen.substr(0, fen.find(' '));
    float score = 0.0;
    for(int i = 0; i < first_token.length(); i++){
        if(first_token[i] == 'p'){
            score -= 2.0;
        }
        else if(first_token[i] == 'P'){
            score += 2.0;
        }
        else if(first_token[i] == 'n'){
            score -= 6.0;
        }
        else if(first_token[i] == 'N'){
            score += 6.0;
        }
        else if(first_token[i] == 'b'){
            score -= 6.0;
        }
        else if(first_token[i] == 'B'){
            score += 6.0;
        }
        else if(first_token[i] == 'r'){
            score -= 10.0;
        }
        else if(first_token[i] == 'R'){
            score += 10.0;
        }
        else if(first_token[i] == 'q'){
            score -= 18.0;
        }
        else if(first_token[i] == 'Q'){
            score += 18.0;
        }
    }
    return score;
}

float boardMiddleRushCalc(thc::ChessRules &cr){
    std::string fen = cr.ForsythPublish();
    auto first_token = fen.substr(0, fen.find(' '));
    float score = 0.0;
    int alph = 0; //A-H
    int num = 0; //1-8
    // std::cout << "FEN: " << first_token << std::endl;

    for(int i = 0; i < first_token.length(); i++){
        // std::cout << i << ' '<< first_token[i] << ' ' << alph << ' ' << num << std::endl;
        
        
        float squareDistanceFromMiddle = pow((alph - 3.5), 2) + pow((num - 3.5), 2);
        float invDist = 25 - squareDistanceFromMiddle;
        invDist /= 25;

        if(first_token[i] == 'p'){
            score -= 4.0;
            score -= invDist*3;
            alph++;
        }
        else if(first_token[i] == 'P'){
            score += 4.0;
            score += invDist*3;
            alph++;
        }
        else if(first_token[i] == 'n'){
            score -= 12.0;
            score -= invDist*3;
            alph++;
        }
        else if(first_token[i] == 'N'){
            score += 12.0;
            score += invDist*3;
            alph++;
        }
        else if(first_token[i] == 'b'){
            score -= 12.0;
            score -= invDist*2;
            alph++;
        }
        else if(first_token[i] == 'B'){
            score += 12.0;
            score += invDist*2;
            alph++;
        }
        else if(first_token[i] == 'r'){
            score -= 20.0;
            score -= invDist;
            alph++;
        }
        else if(first_token[i] == 'R'){
            score += 20.0;
            score += invDist;
            alph++;
        }
        else if(first_token[i] == 'q'){
            score -= 36.0;
            alph++;
        }
        else if(first_token[i] == 'Q'){
            score += 36.0;
            alph++;
        }
        else if(first_token[i] == 'K' || first_token[i] == 'k'){
            alph++;
        }
        else if(first_token[i] == '/'){
            num++;
            alph = 0;
        }
        else if(first_token[i] == '1'){
            alph++;
        }
        else if(first_token[i] == '2'){
            alph += 2;
        }
        else if(first_token[i] == '3'){
            alph += 3;
        }
        else if(first_token[i] == '4'){
            alph += 4;
        }
        else if(first_token[i] == '5'){
            alph += 5;
        }
        else if(first_token[i] == '6'){
            alph += 6;
        }
        else if(first_token[i] == '7'){
            alph += 7;
        }
        else if(first_token[i] == '8'){
            alph += 8;
        }

    }
    return score;
}

float boardCalc(thc::ChessRules &cr){
    return boardMiddleRushCalc(cr);
}

float minimax(thc::ChessRules &cr, int depth, float alpha, float beta) {
    pos += 1;
    thc::TERMINAL terminal;
    cr.Evaluate(terminal);
    if(terminal == thc::TERMINAL_BCHECKMATE){
        return 10000;
    }
    else if(terminal == thc::TERMINAL_WCHECKMATE){
        return -10000;
    }
    else if(terminal == thc::TERMINAL_WSTALEMATE || terminal == thc::TERMINAL_BSTALEMATE){
        return 0;
    }
    else if(depth == 0){
        return boardCalc(cr);
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
    int bestMoveIdx = 0;
    std::vector<thc::Move> moves;
    cr.GenLegalMoveList(moves);
    unsigned int len = moves.size();
    float alpha = -1000000;
    float beta = 1000000;
    float best = 0;
    if(cr.WhiteToPlay()){
        //maximizing player
        best = -100000;
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            float score = minimax(cr, depth-1, alpha, beta);
            cr.PopMove(moves[i]);
            float prevBest = best;
            best = std::max(best, score);
            alpha = std::max(alpha, best);
            if(prevBest != best){
                bestMoveIdx = i;
            }
        }
    } 
    else {
        //minimizing player
        best = 100000;
        for(int i = 0; i < len; i++){
            cr.PushMove(moves[i]);
            float score = minimax(cr, depth-1, alpha, beta);
            cr.PopMove(moves[i]);
            float prevBest = best;
            best = std::min(best, score);
            beta = std::min(beta, best);
            if(prevBest != best){
                bestMoveIdx = i;
            }
            std::cout << score << std::endl;
        }
    }
    return moves[bestMoveIdx];
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
        thc::Move mv = bestMove(cr, 5);
        cr.PushMove(mv);
        cr.Evaluate(terminal);

        if(terminal != thc::NOT_TERMINAL){
            break;
        }

        std::cout << pos << std::endl;
        pos = 0;
        std::cout << mv.NaturalOut(&cr) << std::endl;
        display_position(cr, "");
        std::cout << boardCalc(cr) << std::endl;

        printf( "List of all legal moves in the current position\n" );
        std::vector<thc::Move> moves;
        std::vector<bool> check;
        std::vector<bool> mate;
        std::vector<bool> stalemate;
        cr.GenLegalMoveList(  moves, check, mate, stalemate );
        unsigned int len = moves.size();
        for( unsigned int i=0; i<len; i++ )
        {
            mv = moves[i];
            std::string mv_txt = mv.NaturalOut(&cr);
            const char *suffix="";
            if( check[i] )
                suffix = " (note '+' indicates check)";
            else if( mate[i] )
                suffix = " (note '#' indicates mate)";
            printf( "4.%s%s\n", mv_txt.c_str(), suffix );
        }
        std::cout << "Enter move: ";
        std::cin >> input;
        mv.NaturalIn(&cr, input.c_str());
        cr.PushMove(mv);
        cr.Evaluate(terminal);
        display_position(cr, "");
        std::cout << boardCalc(cr) << std::endl;
    }
    std::cout << terminal << std::endl;
}

