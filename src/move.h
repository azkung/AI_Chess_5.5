#ifndef MOVE_H_
#define MOVE_H_

#include <iostream>

class Move{
    public:
        Move(int from, int to, int piece, int capturedPiece, bool isCapture, bool isEnPassant, bool isCastle, bool isPromotion, int promotionPiece);
        ~Move();
    private:
        int from;
        int to;
        int piece;
        int capturedPiece;
        bool isCapture;
        bool isCheck;
        bool isCheckmate;
        bool isPromotion;
        bool isCastle;
        bool isEnPassant;
        int promotionPiece;
};

#endif
