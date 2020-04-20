# python3


def hashf(text, pattern, p, x):
    len_p = len(pattern)
    len_t = len(text)
    text = ''.join(reversed(text))
    ind = 0

    hashed_pattern_val = 0
    hashed_text = [0]

    for index, char in enumerate(pattern):
        hashed_pattern_val += ord(char) * (x ** index)

    for index in range(len_t - len_p + 1):
        if index == 0:
            for j in range(len_p - 1, -1, -1):
                hashed_text[0] += ord(text[ind]) * (x ** j)
                ind += 1
            hashed_text[0] = hashed_text[0] % p
        else:
            hashed_text.append(
                ((hashed_text[-1] - ord(text[index - 1]) * (x ** (len_p - 1))) * x + ord(text[index + len_p - 1])) % p)

    return hashed_pattern_val % p, hashed_text


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    res = []
    len_p = len(pattern)
    hashed_pattern_val, hashed_text = hashf(text, pattern, 100000000007, 1)
    for index, val in enumerate(reversed(hashed_text)):
        if hashed_pattern_val == val:
            if text[index:index+len_p] == pattern:
                res.append(index)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

