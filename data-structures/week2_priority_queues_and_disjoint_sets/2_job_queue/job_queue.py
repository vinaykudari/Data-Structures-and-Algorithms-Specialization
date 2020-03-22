# python3

from collections import namedtuple
import heapq

job = namedtuple('job', ['thread', 'finish_time'])


class MinHeap:
    def __init__(self, size):
        self.size = 0
        self.arr = [None] * size

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return i * 2 + 1

    def rightChild(self, i):
        return i * 2 + 2

    def shiftDown(self, index):
        minIndex = index
        r = self.rightChild(index)
        if r < self.size and self.arr[r] < self.arr[minIndex]:
            minIndex = self.rightChild(index)
        l = self.leftChild(index)
        if l < self.size and self.arr[l].finish_time < self.arr[minIndex].finish_time:
            minIndex = self.leftChild(minIndex)

        if self.arr[minIndex] != self.arr[index]:
            self.arr[minIndex], self.arr[index] = self.arr[index], self.arr[minIndex]
            self.shiftDown(minIndex)

    def shiftUp(self, index):
        #         print(f'index = {index}; self.parent(index) = {self.parent(index)}; arr = {self.arr}')
        while self.parent(index) >= 0 and self.arr[self.parent(index)].finish_time > self.arr[index].finish_time:
            self.arr[self.parent(index)], self.arr[index] = self.arr[index], self.arr[self.parent(index)]
            index = self.parent(index)

    #             print(f'Array = {self.arr}; new index = {index}')

    def buildHeap(self):
        for i in range(self.size // 2, -1, -1):
            self.shiftDown(i)

    def extractMin(self):
        if self.size < 0:
            return
        minJob = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        #         print(f'Array before ShiftDown : {self.arr}')
        self.arr[self.size - 1] = None
        self.size -= 1
        self.shiftDown(0)
        #         print(f'Array after ShiftDown : {self.arr}')
        return minJob

    def insert(self, data):
        if self.size >= len(self.arr):
            print("Heap is full")
            return
        #         print(f'inserting data at {self.size}')
        self.arr[self.size] = data
        self.shiftUp(self.size)
        self.size += 1

    #         print(f'Array = {self.arr}')

    def getMin(self):
        return self.arr[0]


def assign_jobs(no_of_threads, job_times):
    start_times = []
    no_of_jobs = len(job_times)
    arr = []
    jobs = []
    n = 0

    for thread_index in range(no_of_threads):
        arr.append(job(thread_index, job_times[thread_index]))
        start_times.append((thread_index, 0))

    mh = MinHeap(no_of_threads)
    for item in arr:
        mh.insert(item)
        n += 1

    while n < no_of_jobs:
        finishedJob = mh.extractMin()
        start_times.append((finishedJob.thread, finishedJob.finish_time))
        heapq.heappush(jobs, finishedJob)
        while mh.size > 0 and mh.getMin().finish_time - finishedJob.finish_time == 0:
            finishedJob = mh.extractMin()
            heapq.heappush(jobs, finishedJob)
        #         print(finishedJob)

        while len(jobs) > 0:
            j = heapq.heappop(jobs)
            mh.insert(job(j.thread, j.finish_time + job_times[n]))
            n = n + 1
    #         print(f'N = {n}')

    return start_times


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for thread, start_time in assigned_jobs:
        print(thread, start_time)


if __name__ == "__main__":
    main()
