# Merkle DAG Implementation in Python

## 📌 Overview
This project implements a **Merkle Directed Acyclic Graph (DAG)** using **Python** and **NetworkX**. The DAG maintains hierarchical relationships between nodes while ensuring data integrity using cryptographic hashing.

## 🔧 Features
- ✅ **Create & Manage a Merkle DAG**
- ✅ **Cryptographic Hashing (SHA-256)** for node integrity
- ✅ **Directed Acyclic Graph (DAG) structure**
- ✅ **Graph Visualization** using `networkx` and `matplotlib`
- ✅ **Automatic Layout Optimization** for better node spacing

## 📦 Installation
Make sure you have **Python 3.x** installed. Then, install dependencies:

```bash
pip install networkx matplotlib
```

## 🚀 Usage
### Run the Python Script
```bash
python merkle_dag.py
```
This will create a Merkle DAG and visualize it as a hierarchical graph.

## 📜 Code Structure
### `MerkleDAGNode` Class
Represents a single node in the DAG.
- Computes a **SHA-256 hash** based on its data and children.
- Stores references to child nodes.

### `MerkleDAG` Class
Handles the **DAG creation, node management, and visualization**.
- **`add_node(data, children=None)`** → Adds a node to the DAG.
- **`visualize_dag()`** → Draws the DAG using **Graphviz layout** (if available) or **shell layout**.

## 🖼️ Visualization
The DAG is displayed using `matplotlib` with **auto-spacing for better readability**. Example:

```
  (a)
  / | \
(b) (c) (d)
 |   |   |
(f)  |   (e)
    (g)
      |
     (h)
      |
     (i)
```

## 🛠️ Troubleshooting
If the graph is **too cluttered**, try **installing Graphviz**:
```bash
brew install graphviz   # MacOS
sudo apt install graphviz  # Ubuntu/Linux
```
This allows `networkx` to use `dot` layout for **cleaner visualization**.

## 📜 License
This project is licensed under the **MIT License**. Feel free to modify and use it!

---
🚀 **Happy Coding!** 🎯

