
from Graph import Graph, Node


def main():

    graph = Graph(name="Algorithms")

    letters  = "ABCDEFGHIJKL"

    for letter in letters:
        graph.add(Node(identifier=letter))

    graph.lookup("A").connect(target=graph.lookup("B"), weight=6)
    graph.lookup("A").connect(target=graph.lookup("C"), weight=8)
    graph.lookup("A").connect(target=graph.lookup("D"), weight=14)

    graph.lookup("B").connect(target=graph.lookup("E"), weight=6)
    graph.lookup("B").connect(target=graph.lookup("F"), weight=2)
    graph.lookup("B").connect(target=graph.lookup("C"), weight=4)

    graph.lookup("C").connect(target=graph.lookup("J"), weight=3)
    graph.lookup("C").connect(target=graph.lookup("G"), weight=7)

    graph.lookup("D").connect(target=graph.lookup("C"), weight=1)
    graph.lookup("D").connect(target=graph.lookup("G"), weight=8)
    graph.lookup("D").connect(target=graph.lookup("H"), weight=8)

    graph.lookup("E").connect(target=graph.lookup("I"), weight=2)
    graph.lookup("E").connect(target=graph.lookup("F"), weight=8)

    graph.lookup("F").connect(target=graph.lookup("I"), weight=9)
    graph.lookup("F").connect(target=graph.lookup("J"), weight=1)
    graph.lookup("F").connect(target=graph.lookup("K"), weight=6)

    graph.lookup("G").connect(target=graph.lookup("H"), weight=11)
    graph.lookup("G").connect(target=graph.lookup("B"), weight=5)

    graph.lookup("H").connect(target=graph.lookup("J"), weight=4)
    graph.lookup("H").connect(target=graph.lookup("L"), weight=2)
    graph.lookup("H").connect(target=graph.lookup("K"), weight=9)

    graph.lookup("I").connect(target=graph.lookup("D"), weight=9)
    graph.lookup("I").connect(target=graph.lookup("D"), weight=3)

    graph.lookup("J").connect(target=graph.lookup("L"), weight=6)
    graph.lookup("J").connect(target=graph.lookup("K"), weight=8)

    graph.lookup("K").connect(target=graph.lookup("L"), weight=2)

    graph.print()


main()
