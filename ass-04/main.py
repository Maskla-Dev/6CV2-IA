
from Graph import Node
from Board import Board


def minimax(root: Node):
    # Con esta pila se realiza un recorrido "en anchura" del árbol,
    # al momento de irse creando.
    stack = [root]              # List [Node]
    while len(stack) > 0:
        # Obtenemos el nodo más próximo y evaluamos el Tablero que contiene.
        current = stack.pop(0)          # Grab Node
        board = current.content         # Grab Board
        while len(board.available) > 0:
            # Por cada lugar disponible se crea una matriz temporal
            # (a partir de la matriz del nodo actual), luego se
            # crea un nodo temporal que se conecta como Hijo al nodo actual.
            index = board.available.pop(0)                          # obtener índice disponible
            tmp_matrix = board.fill(index)                          # creación de matriz temporal
            tmp_turn = "o" if board.turn == "x" else "x"            # decisión de turno (el opuesto al actual)
            tmp_board = Board(matrix=tmp_matrix, turn=tmp_turn)     # tablero temporal
            tmp_child = Node(identifier="", content=tmp_board)      # nodo temporal
            current.connect(target=tmp_child, weight=0)             # conexión como hijo al nodo actual
            stack.append(tmp_child)                                 # agregamos al "recorrido" del árbol
    path = [root]
    while len(path[-1].edges)
        path.push(get_best(path[-1]))


def get_best(node)
    best_move = None
    best_eval = -infinity
    for child in node.edges
        eval = evaluate(child, depth, False)
        if eval > best_eval:
            best_eval = eval
            best_move = child.target
        return best move

def evaluate(edge, depth, is_maximizing_player):
    result = edge.target.content.check_winner()
    if depth == 0 or result != None:
        edge.weight = 1 if result == 'o' else -1
        return edge.weight
    
    if is_maximizing_player:
        max_eval = -infinity
        for child in node.children.edge:
            eval = evaluate(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        edge.weight = max_eval
    else:
        min_eval = +infinity
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        edge.weight = min_eval
        

def main():

    initial_board = ["o", "x", "o",
                     "-", "x", "o",
                     "-", "-", "x"]

    # initial_board = ["o", "x", "-",
    #                  "-", "-", "-",
    #                  "-", "-", "-"]

    initial_node = Node(identifier="", content=Board(matrix=initial_board, turn="o"))
    path = minimax(initial_node)

    initial_node.print_children()
    print(f"{path}")

main()
