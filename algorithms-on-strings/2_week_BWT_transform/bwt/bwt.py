# python3
import sys


def BWT(text):
    bwt_matrix = []
    i = 0

    while i < len(text):
        text = text[-1] + text[:-1]
        bwt_matrix.append(text)
        i += 1
    bwt_matrix.sort()

    return ''.join([text[-1] for text in bwt_matrix])


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
