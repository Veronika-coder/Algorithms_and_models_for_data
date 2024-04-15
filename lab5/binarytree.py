import random

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, key, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key)
        else:
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    return
                else:
                    return self.add_node(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    return
                else:
                    return self.add_node(key, node=node.right)

    def visualize_tree_Knuth(self):
        if self.root is not None:
            self.root.visualize_node(0)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def visualize_node(self, depth):
        if self.right is not None:
            self.right.visualize_node(depth + 1)
        print("   " * depth + "   \___" + f"{self.key:.2f}")
        if self.left is not None:
            self.left.visualize_node(depth + 1)


t = Tree()
for _ in range(7):
    key = random.uniform(10, 50)
    t.add_node(key)

t.visualize_tree_Knuth()
