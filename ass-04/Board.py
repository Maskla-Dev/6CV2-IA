
class Board:

    def __init__(self, matrix, turn):
        self.matrix = matrix      # List[str]
        self.available = []     # List[int]
        self.turn = turn        # str

        for index, fig in enumerate(matrix):
            if fig == "-":      # Empty Square
                self.available.append(index)

    def fill(self, index):
        tmp_matrix = self.matrix[:]
        tmp_matrix[index] = self.turn
        return tmp_matrix

    def print(self, child_factor=0):
        space = child_factor * "  "
        print(f"{space}{self.matrix[0]}|{self.matrix[1]}|{self.matrix[2]}")
        print(f"{space}{self.matrix[3]}|{self.matrix[4]}|{self.matrix[5]}")
        print(f"{space}{self.matrix[6]}|{self.matrix[7]}|{self.matrix[8]}")
        print("")
