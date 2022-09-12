import vars as v


def row(size):
    return [v.blank] * size

class Board:
    def __init__(self, size):
        self.board = [row(size) for _ in range(size)]
        self.size = size

    def display(self):
        for rows in self.board:
            yield ' ' + ' '.join(str(point) for point in rows)

    def __setitem__(self, loc, item):
        self.board[loc.y][loc.x] = item