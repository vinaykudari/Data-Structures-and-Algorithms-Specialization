# python3

import sys
import threading


class Node:
    def __str__(self):
        return str(self.val)

    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, value):
        self.children.append(value)


class Tree:
    def __init__(self):
        self.root = None
        self.node_list = []

    def populate_tree(self):
        for index, parent_node in enumerate(self.node_data):
            if parent_node == -1:
                self.root = self.node_list[index]
                # print(f'Root = {self.root}')
            else:
                self.node_list[parent_node].add_child(self.node_list[index])
                # print(f"Adding child {index} to parent {parent_node}")

    def load_data(self, node_data):
        self.node_data = node_data
        for i in range(len(node_data)):
            self.node_list.append(Node(i))

        self.populate_tree()

    def get_depth(self, node):
        if not node.children:
            return 0

        return 1 + max([self.get_depth(children) for children in node.children])

    def get_height(self):
        return self.get_depth(self.root) + 1


def compute_height(n, parents):
    # Replace this code with a faster implementation
    t1 = Tree()
    t1.load_data(parents)
    max_height = t1.get_height()
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
