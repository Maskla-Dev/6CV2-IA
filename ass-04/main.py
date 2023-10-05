
from Graph import Node
from Board import Board


def minimax(root: Node):
    stack = [root]              # List [Node]
    while len(stack) > 0:
        current = stack.pop(0)          # Grab Node
        board = current.content         # Grab Board
        while len(board.available) > 0:
            index = board.available.pop(0)
            tmp_matrix = board.fill(index)
            tmp_turn = "o" if board.turn == "x" else "x"
            tmp_board = Board(matrix=tmp_matrix, turn=tmp_turn)
            tmp_child = Node(identifier="", content=tmp_board)
            current.connect(target=tmp_child, weight=0)
            stack.append(tmp_child)


def main():

    # initial_board = ["o", "x", "o",
    #                  "-", "x", "o",
    #                  "-", "-", "x"]

    initial_board = ["o", "x", "-",
                     "-", "-", "-",
                     "-", "-", "-"]

    initial_node = Node(identifier="", content=Board(matrix=initial_board, turn="x"))
    minimax(initial_node)

    initial_node.print_children()


main()