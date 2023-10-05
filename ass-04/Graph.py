
class Edge:

    def __init__(self, source, target, weight):
        self.source = source    # Node
        self.target = target    # Node
        self.weight = weight    # int

    def __str__(self):
        return f"{self.source} to {self.target} costs {self.weight}"


class Node:

    def __init__(self, identifier, content = None):
        # ID
        self.identifier = identifier    # str
        # Status
        self.state = {                  # Dict[str, bool]
            "visited": False
        }
        # Content
        self.content = content
        # Edge Lookup
        self.edges = []                 # List[Edge]

    def __str__(self):
        return f"{self.identifier}"

    def print_children(self, child_factor=0):
        self.content.print(child_factor)
        for edge in self.edges:
            edge.target.print_children(child_factor+1)

    def lookup(self, identifier):       # -> Edge or None
        for edge in self.edges:
            if edge.target.identifier == identifier:
                return edge
        return None

    def connect(self, target, weight):  # target: Node, weight: int
        self.edges.append(Edge(self, target, weight))
        # this condition only works when using unique identifiers for each node
        # if self.lookup(target.identifier) is None:
        #     self.edges.append(Edge(self, target, weight))


class Graph:

    def __init__(self, name):
        # ID
        self.name = name        # str
        # Node Lookup
        self.nodes = []         # List[Node]

    def print(self):
        for node in self.nodes:
            print(node)
            for edge in node.edges:
                print(f"  {edge}")

    def lookup(self, identifier):     # -> Node or None
        for node in self.nodes:
            if node.identifier == identifier:
                return node
        return None

    def add(self, node):
        if self.lookup(node.identifier) is None:
            self.nodes.append(node)

    def connect(self, id1, id2, weight):
        if self.lookup(id1) is None:
            raise AttributeError(f"Graph does not contains Node {id1}")
        if self.lookup(id2) is None:
            raise AttributeError(f"Graph does not contains Node {id2}")
        self.lookup(id1).connect(target=self.lookup(id2), weight=weight)
        self.lookup(id2).connect(target=self.lookup(id1), weight=weight)

    def reset(self):
        for node in self.nodes:
            node.state["visited"] = False
