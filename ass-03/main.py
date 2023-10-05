import random

from Graph import Graph, Node


def hill_climbing(graph: Graph, start: str, finish: str, minmax: str = "min"):

    current = graph.lookup(start)
    travel = []

    travel += current.identifier

    while current.identifier != finish:

        contestants_min = []
        contestants_max = []

        if len(current.edges) > 0:
            max_cost = min_cost = current.edges[0].weight

            # Find the lowest cost
            for edge in current.edges:
                if edge.weight < min_cost:
                    min_cost = edge.weight
                if edge.weight > max_cost:
                    max_cost = edge.weight

            # Find transitions
            for edge in current.edges:
                if edge.weight == min_cost:
                    contestants_min.append(edge.target)
                if edge.weight == max_cost:
                    contestants_max.append(edge.target)

        if minmax == "max":
            current = random.choice(contestants_max)
        else:
            current = random.choice(contestants_min)

        travel += current.identifier

    print(travel)


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

    hill_climbing(graph, "A", "L", "min")
    hill_climbing(graph, "A", "L", "max")


main()
