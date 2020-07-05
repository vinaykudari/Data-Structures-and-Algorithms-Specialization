# python3
import sys


def get_prefix_array(str, str_len):
    prefix_array = [0] * str_len
    border = 0

    for i in range(1, str_len):
        while border > 0 and str[i] != str[border]:
            border = prefix_array[border - 1]
        if str[i] == str[border]:
            border += 1
        else:
            border = 0
        prefix_array[i] = border

    return prefix_array


def find_pattern(pattern, text):
    """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
    res = []
    S = pattern + '$' + text
    S_len = len(S)
    pattern_len = len(pattern)

    s = get_prefix_array(S, S_len)

    for i in range(pattern_len, S_len):
        if s[i] == pattern_len:
            res.append(i-(2*pattern_len))

    return res


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
