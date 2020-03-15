# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.tail
            self.tail = Node(data)
            node.next = self.tail
        self.len += 1

    def dequeue(self):
        if not self.head:
            # print('Queue is empty')
            return
        else:
            val = self.head.val
            if self.len == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.len -= 1
            return val

    def last(self):
        return self.tail.val

    def first(self):
        return self.head.val

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = Queue()
        self.buffer_time = Queue()

    def process(self, request):
        flag = True
        if self.finish_time.isEmpty():
            self.finish_time.enqueue(request.time_to_process)
            self.buffer_time.enqueue(request.time_to_process)
            return Response(False, request.arrived_at)
        if request.arrived_at >= self.finish_time.last():
            while flag:
                flag = self.finish_time.dequeue()
            self.finish_time.enqueue(request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)
        else:
            if request.arrived_at >= self.buffer_time.last():
                self.finish_time.dequeue()
                self.buffer_time.dequeue()
            if self.finish_time.len == self.size:
                return Response(True, -1)
            start_time = self.finish_time.last()
            self.buffer_time.enqueue(self.finish_time.last() - request.arrived_at + request.time_to_process)
            self.finish_time.enqueue(self.finish_time.last() + request.time_to_process)
            return Response(False, start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
