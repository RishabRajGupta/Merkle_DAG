import hashlib
import json
import networkx as nx
import matplotlib.pyplot as plt

class MerkleDAGNode:
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children if children else []
        self.hash = self.compute_hash()

    def compute_hash(self):
        hasher = hashlib.sha256()
        hasher.update(json.dumps(self.data, sort_keys=True).encode('utf-8'))
        for child in self.children:
            hasher.update(child.hash.encode('utf-8'))
        return hasher.hexdigest()

    def add_child(self, child):
        self.children.append(child)
        self.hash = self.compute_hash()

    def __repr__(self):
        return f"Node({self.data})"

class MerkleDAG:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data, children=None):
        node = MerkleDAGNode(data, children)
        self.nodes[node.hash] = node
        return node

    def visualize_dag(self):
        G = nx.DiGraph()
        label_map = {}

        for node in self.nodes.values():
            label_map[node.hash] = node.data
            for child in node.children:
                G.add_edge(node.hash, child.hash)

        plt.figure(figsize=(12, 8))  # Bigger figure size for readability

        try:
            pos = nx.nx_agraph.graphviz_layout(G, prog="dot")  # Use Graphviz if available
        except:
            pos = nx.shell_layout(G)  # Fallback to shell layout if Graphviz isn't installed

        nx.draw(G, pos, with_labels=True, labels=label_map, node_size=2500, node_color="lightblue",
                font_size=12, font_weight="bold", edge_color="black", arrows=True)

        plt.show()

# Example DAG Construction (Expanded)
dag = MerkleDAG()

# Root node
node_a = dag.add_node("a")

# Intermediate nodes
node_b = dag.add_node("b")
node_c = dag.add_node("c")
node_d = dag.add_node("d", [node_b, node_c])
node_e = dag.add_node("e", [node_d, node_c])

# More intermediate nodes
node_f = dag.add_node("f", [node_b])
node_g = dag.add_node("g", [node_c, node_f])
node_h = dag.add_node("h", [node_d, node_g])
node_i = dag.add_node("i", [node_h])
node_j = dag.add_node("j", [node_g, node_h])
node_k = dag.add_node("k", [node_j, node_e])  # Connecting multiple branches

# Connect root to various nodes
node_a.add_child(node_b)
node_a.add_child(node_c)
node_a.add_child(node_d)
node_a.add_child(node_f)

# Visualize the DAG
dag.visualize_dag()
