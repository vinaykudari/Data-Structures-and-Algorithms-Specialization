# python3
import sys
from collections import defaultdict

NA = -1


def build_trie(patterns):
    trie = defaultdict(dict)
    node_number = 0
    # write your code here
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if current_symbol not in trie[current_node]:
                trie[current_node][current_symbol] = node_number + 1
                node_number += 1
                current_node = trie[current_node][current_symbol]
            else:
                current_node = trie[current_node][current_symbol]
        trie[current_node]['$'] = node_number + 1

    return trie


def solve(text, n, patterns):
    trie = build_trie(patterns)
    result = []
    text_len = len(text)

    for index in range(text_len):
        current_node = 0
        text_index = index
        while text_index < text_len and text[text_index] in trie[current_node]:
            ch = text[text_index]
            if ch in trie[current_node]:
                current_node = trie[current_node][ch]
                text_index += 1
                if '$' in trie[current_node]:
                    result.append(index)
                    break

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
