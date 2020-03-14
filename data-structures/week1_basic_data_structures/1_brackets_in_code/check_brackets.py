# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


class Stack:
    def __init__(self, size):
        self.top = -1
        self.arr = [None] * size

    def push(self, data):
        if self.top == len(self.arr) - 1:
            print('Stack is full')
            return
        else:
            self.top = self.top + 1
            self.arr[self.top] = data

    #         print(self.arr)

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            val = self.arr[self.top]
            self.arr[self.top] = None
            self.top = self.top - 1
            return val

    def topp(self):
        return self.arr[self.top]


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    s1 = Stack(len(text))
    for i, next in enumerate(text):
        if next in "([{":
            s1.push({'value': next, 'index': i + 1})

        if next in ")]}":
            if s1.top == -1:
                return i + 1

            left = s1.pop().get('value')
            right = next

            if not are_matching(left, right):
                return i + 1

    if s1.top == -1:
        return 'Success'
    else:
        return s1.arr[s1.top].get('index')


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
