import numpy as np

class State:
    def __init__(self, board):
        self.board = board # np.array
        self.rows, self.cols = board.shape
        self.g = 0
        self.h = 0
        self.f = 0
        self.action = None
        self.set_blank_pos()

    def get_blank_pos (self):
        # if self.blank_pos:
        #     return self.blank_pos
        # pos = np.where(self.board == 0)
        # row = pos[0].item()
        # col = pos[1].item()
        # self.blank_pos = row, col
        return self.blank_pos

    def set_blank_pos (self):
        pos = np.where(self.board == 0)
        row = pos[0].item()
        col = pos[1].item()
        self.blank_pos = row, col
        # return row, col

    def tilesNotInPlace (self):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.rows * row + col != self.board[row,col] and self.board[row,col] !=0:
                    count += 1
        self.h = count
        self.f = self.h + self.g
        return count

    def ManhatanDistance (self):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                targetRow, targetCol = self.board[row,col] // self.rows, self.board[row,col] % self.rows
                count += abs(row-targetRow)+ abs(col-targetCol)
        self.h = count
        self.f = self.h + self.g
        return count

    def calc_h (self, Heuristic = tilesNotInPlace):
        return Heuristic(self)


    def __eq__(self, other):
        return np.equal(self.board, other.board).all()

    def copy (self):
        newBoard = np.copy(self.board)
        return State (newBoard)

    def __hash__(self) -> int:
        return hash(repr(self.board))
