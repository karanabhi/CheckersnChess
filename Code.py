int GetValue(board, ColorMoving) for (byte x= 0; x ¡ 8; x++) for (byte y = 0; y¡ 8; y++) 
BoardSquare square = board. GetPosition(x,y); if (NoPieceOnSquare) coninue; 
if (square.CurrentPiece.PieceColor ==White) Value += GetPieceValue(square, x, y); if(y ==7)board.WhiteWins = true; if(y == 0)Value += HomeGroundValue; if (column ¿ 0) ThreatA = (board[GetPosition(y - 1, 7).NoPieceOnSquare); if (column ¡ 7) ThreatB = (board.GetPosition(y + 1, 7).NoPieceOnSquare); if (ThreatA and ThreatB) board.Value += PieceAlmostWinValue; if (WhitePiecesOnColumn == 0)Value -= PieceColumnHoleValue; if (BlackPiecesOnColumn == 0)Value += PieceColumnHoleValue; if (RemainingWhitePieces == 0) board.BlackWins = true; if (RemainingBlackPieces == 0) board.WhiteWins = true; if (board.WhiteWins)Value += WinValue; if (board.BlackWins)Value -= WinValue; 
int GetPieceValue(square, Column, Row) int Value = PieceValue; var Piece = square.CurrentPiece; if (Piece.ConnectedH) Value += PieceConnectionHValue; if (Piece.ConnectedV) Value += PieceConnectionVValue; Value += Piece.ProtectedValue; if (Piece.AttackedValue ¿ 0) Value -= Piece.AttackedValue; if (Piece.ProtectedValue == 0) Value -= Piece.AttackedValue; else if (Piece.ProtectedValue != 0) if (Piece.PieceColor == White) if (Row == 5) Value += PieceDangerValue; else if (Row == 6) Value += PieceHighDangerValue;else if (Row == 2) Value += PieceDangerValue; else if (Row == 1) Value += PieceHighDangerValue; 
class AlphaBeta(GameTreeSearcher): def getBestActionAndValue(self, currentState): 
self.player = currentState.currentPlayer() 
return self.maximin(currentState, -1, 1) 
def maximin(self, currentState, alpha, beta): utility = currentState.utility() if utility: return None, utility[self.player] 
bestAction = None for (action, succ) in currentState.successors(): 
val = self.minimax(succ, alpha, beta)[1] if val ¿ alpha: 
bestAction, alpha = action, val if alpha ¿= beta: break return bestAction, alpha 
def minimax(self, currentState, alpha, beta): utility = currentState.utility() if utility: return None, utility[self.player] 
bestAction = None for (action, succ) in currentState.successors(): 
val = self.maximin(succ, alpha, beta)[1] if val ¡ beta: 
bestAction, beta = action, val if alpha ¿= beta: break return bestAction, beta 