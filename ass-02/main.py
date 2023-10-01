
from Graph import Node, Graph


def depth_first(graph: Graph, start: str):

    root: Node = graph.lookup(start)

    stack = []      # List[Node]
    path = ""

    stack.append(root)
    root.state["visited"] = True

    while len(stack) > 0:
        handle = stack.pop()        # use LIFO behavior
        path += handle.identifier
        for edge in handle.edges:
            neighbor = edge.walk()
            if not neighbor.state["visited"]:
                stack.append(neighbor)
                neighbor.state["visited"] = True

    print(path)


def breadth_first(graph: Graph, start: str):

    root: Node = graph.lookup(start)

    stack = []
    path = ""

    stack.append(root)
    root.state["visited"] = True

    while len(stack) > 0:
        handle = stack.pop(0)       # use FIFO behavior
        path += handle.identifier
        for edge in handle.edges:
            neighbor = edge.walk()
            if not neighbor.state["visited"]:
                stack.append(neighbor)
                neighbor.state["visited"] = True

    print(path)


def main():

    graph = Graph(name="Graph Test")

    letters = "ABCDEFGHIJK"

    for letter in letters:
        graph.add(Node(identifier=letter))

    graph.connect("A", "B", 1)
    graph.connect("A", "C", 1)
    graph.connect("B", "D", 1)
    graph.connect("B", "E", 1)
    graph.connect("E", "H", 1)
    graph.connect("E", "I", 1)
    graph.connect("C", "F", 1)
    graph.connect("C", "G", 1)
    graph.connect("F", "J", 1)
    graph.connect("F", "K", 1)

    # graph.print()

    depth_first(graph, "A")
    graph.reset()
    breadth_first(graph, "A")


main()
