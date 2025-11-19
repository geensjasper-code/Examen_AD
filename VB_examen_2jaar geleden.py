import heapq
from functools import total_ordering

class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self):
        return f"Edge({self.node1}, {self.node2}, {self.weight})"

    def __repr__(self):
        return self.__str__()


class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        edge = Edge(node1, node2, weight)
        self.adjacency_list[node1].append(edge)

    def get_all_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        return self.adjacency_list.get(node, [])

    def __str__(self):
        result = ""
        for node, edges in self.adjacency_list.items():
            result += f"{node} -> {[(edge.node2, edge.weight) for edge in edges]}\n"
        return result

@total_ordering
class SpecialSorted:

    def __init__(self, element, value):
        self.element = element
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

class PriorityQueue:

    def __init__(self, sortkey=lambda x: x):
        self.content = []
        self.sortkey = sortkey

    def add(self, item):
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def peek(self):
        return self.content[0].element if self.content else None

    def poll(self):
        return heapq.heappop(self.content).element if self.content else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str([(item.element[0], item.element[1]) for item in self.content])

def shortest_path(graph: DirectedGraph, src: Node, dest: Node) -> list | None:
    if src == dest:
        return [src]

    node_dist = {node: float('inf') for node in graph.get_all_nodes()} #afstand van alle nodes naar elkaar op oneindig zetten
    previous_nodes = {node: None for node in graph.get_all_nodes()} # alle linken tussen de nodes verbreken (denk ik)
    node_dist[src] = 0 # afstand tot de bronnode of waar we beginnen op 0 zetten

    # Priority queue with (node, distance) tuples
    queue = PriorityQueue(sortkey=lambda x: x[1])
    queue.add((src, 0))

    while not queue.is_empty():
        current_node, current_dist = queue.poll()

        if current_node == dest:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return path

        for edge in graph.get_outgoing_edges(current_node):
            neighbor = edge.node2
            new_dist = current_dist + edge.weight

            if new_dist < node_dist[neighbor]:
                node_dist[neighbor] = new_dist
                previous_nodes[neighbor] = current_node
                queue.add((neighbor, new_dist))
    return None