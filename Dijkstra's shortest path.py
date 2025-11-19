import heapq
from functools import total_ordering

# -------------------------
# Priority Queue
# -------------------------
@total_ordering
class SpecialSorted:
    """
    Wrapper voor elementen in de priority queue.
    Zorgt dat elementen vergeleken kunnen worden op hun 'value'.
    """
    def __init__(self, element, value):
        self.element = element  # het originele element (bijv. (Node, afstand))
        self.value = value      # de prioriteit (bijv. afstand tot src)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

class PriorityQueue:
    """
    Eenvoudige priority queue gebaseerd op heapq.
    Elementen worden gesorteerd op de sortkey.
    """
    def __init__(self, sortkey=lambda x: x):
        self.content = []
        self.sortkey = sortkey

    def add(self, item):
        """Voeg een item toe met de prioriteit bepaald door sortkey"""
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def peek(self):
        """Bekijk het element met de hoogste prioriteit zonder het te verwijderen"""
        return self.content[0].element if self.content else None

    def poll(self):
        """Haal het element met de hoogste prioriteit op en verwijder het"""
        return heapq.heappop(self.content).element if self.content else None

    def is_empty(self):
        """Controleer of de queue leeg is"""
        return len(self.content) == 0

# -------------------------
# Graph classes
# -------------------------
class Node:
    """Representeert een knoop in een graaf"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __hash__(self):
        return hash(self.value)  # Nodig om Node in sets en dicts te gebruiken

class Edge:
    """Representeert een gerichte gewogen edge"""
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

class DirectedGraph:
    """Eenvoudige gerichte gewogen graaf"""
    def __init__(self):
        self.nodes = set()
        self.adjacency_list = {}  # map van node -> lijst van uitgaande edges

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight):
        """Voeg een gerichte edge toe van node1 naar node2 met gewicht"""
        self.add_node(node1)
        self.add_node(node2)
        self.adjacency_list[node1].append(Edge(node1, node2, weight))

    def get_all_nodes(self):
        """Retourneer alle nodes in de graaf"""
        return self.nodes

    def get_outgoing_edges(self, node):
        """Retourneer alle uitgaande edges van een node"""
        return self.adjacency_list.get(node, [])

# -------------------------
# Dijkstra shortest path
# -------------------------
def shortest_path(graph, src, dest):
    """
    Bepaal het kortste pad van src naar dest in een gerichte gewogen graaf graph.
    Geeft een lijst van Nodes terug die het pad vormen, of None als er geen pad is.
    """
    if src == dest:
        return [src]  # trivial case: begin = eind

    # Initialiseer afstanden naar alle nodes op oneindig
    node_dist = {node: float('inf') for node in graph.get_all_nodes()}
    previous_nodes = {node: None for node in graph.get_all_nodes()}  # voor pad reconstructie
    node_dist[src] = 0  # afstand naar startnode = 0

    # Priority queue: (node, afstand)
    queue = PriorityQueue(sortkey=lambda x: x[1])
    queue.add((src, 0))

    while not queue.is_empty():
        current_node, current_dist = queue.poll()

        # Vroegtijdig stoppen als we de bestemming hebben bereikt
        if current_node == dest:
            path = []
            # reconstructie van het pad van dest naar src
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return path

        # Update afstanden voor alle buren
        for edge in graph.get_outgoing_edges(current_node):
            neighbor = edge.node2
            new_dist = current_dist + edge.weight
            if new_dist < node_dist[neighbor]:
                node_dist[neighbor] = new_dist
                previous_nodes[neighbor] = current_node
                queue.add((neighbor, new_dist))  # update queue

    return None  # Geen pad gevonden

# -------------------------
# Voorbeeldgebruik
# -------------------------
if __name__ == "__main__":
    # Maak een voorbeeldgraaf
    graph = DirectedGraph()
    a = Node("Alice")
    b = Node("Bob")
    c = Node("Carol")

    graph.add_edge(a, b, 5)
    graph.add_edge(b, c, 5)
    graph.add_edge(c, a, 5)

    src = c
    dest = a

    path = shortest_path(graph, src, dest)
    print("Kortste pad:", path)  # Output: [Node('Carol'), Node('Alice')]
