#python3
import sys


class Stack:
    def __init__(self, size):
        self.top = -1
        self.arr = [None]*size
        self.max = 0

    def push(self, data):
        if self.top == len(self.arr)-1:
            return
        else:
            self.top = self.top + 1
            self.arr[self.top] = data
        if data > self.max:
            self.max = data

    def pop(self):
        if self.top == -1:
            return
        else:
            val = self.arr[self.top]
            self.arr[self.top] = None
            self.top = self.top - 1
            return val

    def Max(self):
        return self.max


if __name__ == '__main__':
    num_queries = int(sys.stdin.readline())
    stack = Stack(num_queries)
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
