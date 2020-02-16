# Uses python3
def edit_distance(s, t):
    table = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    for i in range(len(t) + 1):
        table[0][i] = i

    for j in range(len(s) + 1):
        table[j][0] = j

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] != t[j - 1]:
                table[i][j] = min(table[i][j - 1] + 1, table[i - 1][j] + 1, table[i - 1][j - 1] + 1)
            elif s[i - 1] == t[j - 1]:
                table[i][j] = table[i - 1][j - 1]

    return table[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
