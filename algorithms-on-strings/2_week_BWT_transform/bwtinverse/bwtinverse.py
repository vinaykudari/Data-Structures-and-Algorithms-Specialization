# python3
import sys


def get_text_with_index(text):
    hash_map = {}
    text_with_index = []
    for ch in text:
        hash_map[ch] = hash_map.get(ch, 0) + 1
        text_with_index.append(ch + str(hash_map[ch]))

    return text_with_index


def InverseBWT(bwt):
    # write your code here
    hash_map = {}
    result = ''
    bwt_with_index = get_text_with_index(bwt)
    first_col_with_index = get_text_with_index(sorted(bwt))

    for i in range(len(bwt)):
        hash_map[first_col_with_index[i]] = bwt_with_index[i]

    ch = '$1'

    while hash_map[ch] != '$1':
        result += hash_map[ch][0]
        ch = hash_map[ch]

    return result[::-1] + '$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
