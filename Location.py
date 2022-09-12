class Location:
    def __init__(self, x, y):
        if isinstance(x, str):
            self.x = 'abcdefgh'.index(x)
            self.y = int(y) - 1
        else:
            self.x, self.y = x, y
    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        x = 'abcdefgh'[self.x]
        return f'{x}{self.y + 1}'

