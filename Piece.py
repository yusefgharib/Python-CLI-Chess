import vars as v
from Location import Location
class Piece:
    def __init__(self, color, location, board):
        self.color = color
        self.location = location
        self.board = board
        self.first_move = True

    def __repr__(self):
        char = piece_data[self.__class__][0]
        return char[0 if self.color == v.WHITE else 1]


class Rook(Piece):
    pass


class Bishop(Piece):
    pass


class Knight(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


class Pawn(Piece):
    pass

