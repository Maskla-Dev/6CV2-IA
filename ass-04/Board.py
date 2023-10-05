
class Board:

    def __init__(self, board, turn):
        self.board = board      # List[str]
        self.available = []     # List[int]
        self.turn = turn        # str

        for index, fig in enumerate(board):
            if fig == "-":      # Empty Square
                self.available.append(index)

    def fill(self, index):
        self.board[index] = "o" if self.turn == "min" else "x"

    def print(self):
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        print("-----")
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print("-----")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")
