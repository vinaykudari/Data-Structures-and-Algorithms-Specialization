#Uses python3
import sys
from collections import defaultdict

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    populated_tree = defaultdict(dict)
    node_number = 0
    # write your code here
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if current_symbol not in populated_tree[current_node]:
                populated_tree[current_node][current_symbol] = node_number + 1
                node_number += 1
                current_node = populated_tree[current_node][current_symbol]
            else:
                current_node = populated_tree[current_node][current_symbol]

    return populated_tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
