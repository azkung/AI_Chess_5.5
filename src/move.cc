#include "move.h"


Move::Move(int from, int to, int piece, int capturedPiece = 0, bool isCapture = false, bool isEnPassant = false, bool isCastle = false, bool isPromotion = false, int promotionPiece = 0) {
    this->from = from;
    this->to = to;
    this->piece = piece;
    this->capturedPiece = capturedPiece;
    this->isCapture = isCapture;
    this->isEnPassant = isEnPassant;
    this->isCastle = isCastle;
    this->isPromotion = isPromotion;
    this->promotionPiece = promotionPiece;
}

Move::~Move() {}