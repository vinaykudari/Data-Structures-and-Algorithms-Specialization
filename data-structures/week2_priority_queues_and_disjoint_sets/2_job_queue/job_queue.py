# python3

from collections import namedtuple

item = namedtuple('item', ['val', 'priority'])


class MinHeap:
    def __init__(self):
        self.size = 0
        self.arr = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return i * 2 + 1

    def rightChild(self, i):
        return i * 2 + 2

    def shiftDown(self, index):
        minIndex = index
        l = self.leftChild(index)
        if l < self.size and self.arr[l].priority < self.arr[minIndex].priority:
            minIndex = self.leftChild(minIndex)
        r = self.rightChild(index)
        if r < self.size and self.arr[r].priority < self.arr[minIndex].priority:
            minIndex = self.rightChild(index)
        #         print(f'minIndex = {minIndex}; index = {index}')
        if minIndex != index:
            self.arr[minIndex], self.arr[index] = self.arr[index], self.arr[minIndex]
            self.shiftDown(minIndex)

    def shiftUp(self, index):
        #         print(f'index = {index}; self.parent(index) = {self.parent(index)}; arr = {self.arr}')
        while self.parent(index) >= 0 and self.arr[self.parent(index)].priority > self.arr[index].priority:
            self.arr[self.parent(index)], self.arr[index] = self.arr[index], self.arr[self.parent(index)]
            index = self.parent(index)

    #             print(f'Array = {self.arr}; new index = {index}')

    def buildHeap(self):
        for i in range(self.size // 2, -1, -1):
            self.shiftDown(i)

    def extractMin(self):
        if self.size <= 0:
            return
        minJob = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        #         print(f'Array before ShiftDown : {self.arr}')
        self.arr.remove(self.arr[self.size - 1])
        self.size -= 1
        self.shiftDown(0)
        #         print(f'Array after ShiftDown : {self.arr}')
        return minJob

    def insert(self, data):
        #         print(f'inserting data at {self.size}')
        self.arr.append(data)
        self.shiftUp(self.size)
        self.size += 1

    #         print(f'Array = {self.arr}')

    def getMin(self):
        return self.arr[0]


def assign_jobs(no_of_threads, job_times):
    start_times = []
    no_of_jobs = len(job_times)
    arr = []
    n = 0

    job_heap = MinHeap()
    thread_heap = MinHeap()

    for thread_index in range(min(no_of_threads, no_of_jobs)):
        arr.append(item(thread_index, job_times[thread_index]))
        start_times.append((thread_index, 0))

    for job in arr:
        job_heap.insert(job)
        n += 1

    # print(f'Job Heap = {job_heap.arr}')

    while n < no_of_jobs:
        finishedJob = job_heap.extractMin()
        #     print(f'Extracting Job with min finish time from Job Heap : {finishedJob}')
        # start_times.append((finishedJob.val, finishedJob.priority))
        #     print(f'Inserting into thread heap; Thread Heap = {thread_heap.arr}')
        thread_heap.insert(item(finishedJob.priority, finishedJob.val))
        while job_heap.size > 0 and job_heap.getMin().priority - finishedJob.priority == 0:
            finishedJob = job_heap.extractMin()
            #         print(f'Extracting Job with min finish time from Job Heap : {finishedJob}')
            thread_heap.insert(item(finishedJob.priority, finishedJob.val))
            # start_times.append((finishedJob.val, finishedJob.priority))

        #     print(f'\nN = {n}; Thread Heap = {thread_heap.arr}; Thread Heap Size = {thread_heap.size}; Job Heap = {job_heap.arr} \n')

        while thread_heap.size > 0:
            j = thread_heap.extractMin()
            start_times.append((j.priority, j.val))
            job_heap.insert(item(j.priority, j.val + job_times[n]))
            #         print(f'Extracting thread with min index from Thread Heap : {j} amd inserting to Job Heap {job_heap.arr}')
            n = n + 1
    #         print(f'N = {n}; Thread Heap = {thread_heap.arr};\n')

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
