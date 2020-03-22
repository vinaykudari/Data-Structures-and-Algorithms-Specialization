# python3


class MinHeap:
    def __init__(self, size):
        self.size = size
        self.arr = []
        self.swaps = []

    def parent(self, i):
        return i - 1 // 2

    def leftChild(self, i):
        return i * 2 + 1

    def rightChild(self, i):
        return i * 2 + 2

    def shiftDown(self, index):
        minIndex = index
        l = self.leftChild(index)
        #         print(f'Left Child Index = {l}; Min Index = {minIndex}; Array = {self.arr}')
        if l < self.size and self.arr[l] < self.arr[minIndex]:
            minIndex = self.leftChild(minIndex)
        r = self.rightChild(index)
        if r < self.size and self.arr[r] < self.arr[minIndex]:
            minIndex = self.rightChild(index)

        if self.arr[minIndex] != self.arr[index]:
            self.swaps.append((index, minIndex))
            self.arr[minIndex], self.arr[index] = self.arr[index], self.arr[minIndex]
            self.shiftDown(minIndex)

    def getSwaps(self):
        return self.swaps


def build_heap(data):
    mh = MinHeap(len(data))
    mh.arr = data

    for i in range(mh.size // 2, -1, -1):
        mh.shiftDown(i)

    return mh.swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
