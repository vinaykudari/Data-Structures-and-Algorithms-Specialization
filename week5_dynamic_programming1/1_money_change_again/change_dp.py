# Uses python3
import sys


def money_change(change_amount):
    coin_set = [1, 3, 4]
    table = [[0 for j in range(change_amount + 1)] for i in range(0, len(coin_set) + 1)]

    # no of 1 rupee coins required to get corresponding changes
    for i in range(change_amount + 1):
        table[0][i] = i

    for coin_index in range(1, len(coin_set) + 1):
        for amount in range(1, change_amount + 1):
            if coin_set[coin_index - 1] == amount:
                table[coin_index][amount] = 1

            if coin_set[coin_index - 1] > amount:
                table[coin_index][amount] = table[coin_index - 1][amount]

            if coin_set[coin_index - 1] < amount:
                table[coin_index][amount] = min(table[coin_index - 1][amount],
                                                1 + table[coin_index][amount - coin_set[coin_index - 1]])

    return table[-1][-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(money_change(m))
