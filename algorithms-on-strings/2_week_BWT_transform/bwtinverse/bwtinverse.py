# python3
import sys


def get_text_with_index(text):
    hash_map = {}
    text_with_index = []
    for ch in text:
        hash_map[ch] = hash_map.get(ch, 0) + 1
        text_with_index.append(ch + str(hash_map[ch]))

    return text_with_index


def count_sort(arr, arr_len):
    min_index, max_index = min(arr), max(arr)
    res = [0] * arr_len

    for i in range(arr_len):
        arr[i] -= min_index

    count_arr = [0]*(max_index-min_index+1)
    for i in arr:
        count_arr[i] += 1

    cum_sum = 0
    for i in range(len(count_arr)):
        cum_sum += count_arr[i]
        count_arr[i] = cum_sum

    for i in count_arr[::-1]:
        res[i-1] = chr(max_index)
        max_index -= 1

    for i in range(arr_len-2, -1, -1):
        if res[i] == 0:
            res[i] = res[i+1]

    return ''.join(res)


def get_int_array_from_text(text):
    return[ord(ch) for ch in text]


def InverseBWT(bwt):
    # write your code here
    hash_map = {}
    text_len = len(bwt)
    result = []

    bwt_with_index = get_text_with_index(bwt)
    first_col_with_index = get_text_with_index(count_sort(get_int_array_from_text(bwt), text_len))
    for i in range(text_len):
        hash_map[first_col_with_index[i]] = bwt_with_index[i]

    ch = '$1'

    while hash_map[ch] != '$1':
        result.append(hash_map[ch][0])
        ch = hash_map[ch]

    return ''.join(result[::-1]) + '$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
