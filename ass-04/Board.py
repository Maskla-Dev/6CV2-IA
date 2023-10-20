
class Board:

    def __init__(self, matrix, turn):
        self.matrix = matrix      # List[str]
        self.available = []     # List[int]
        self.turn = turn        # str

        for index, fig in enumerate(matrix):
            if fig == "-":      # Empty Square
                self.available.append(index)

    def fill(self, index):
        tmp_matrix = self.matrix[:]     # generar una deep copy, no una referencia
        tmp_matrix[index] = self.turn
        return tmp_matrix

    def print(self, child_factor=0):
        space = child_factor * "  "
        print(f"{space}{self.matrix[0]}|{self.matrix[1]}|{self.matrix[2]}")
        print(f"{space}{self.matrix[3]}|{self.matrix[4]}|{self.matrix[5]}")
        print(f"{space}{self.matrix[6]}|{self.matrix[7]}|{self.matrix[8]}")
        print("")
        
    def check_winner(self):
        # Define the winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

        for combination in winning_combinations:
            a, b, c = combination
            if self.matrix[a] == self.matrix[b] == self.matrix[c] and self.matrix[a] != "-":
                return self.matrix[a]  # Return the winning symbol (X or O)

        return None  # No winner yet
