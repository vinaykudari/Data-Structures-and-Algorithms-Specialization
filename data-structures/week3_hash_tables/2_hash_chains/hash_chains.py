# python3


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            self.head = Node(data)
            self.head.next = node

    def insert_at(self, pos, data):
        node = self.head
        if pos == 0:
            self.head = Node(data)
            self.head.next = node
        else:
            while pos - 1 > 0:
                node = node.next
                pos = pos - 1
            next_node = node.next
            node.next = Node(data)
            node.next.next = next_node

    def pop_front(self):
        if self.head is None:
            print('LinkedList is Empty')
            return
        node = self.head
        self.head = self.head.next

    def traverse(self):
        node = self.head
        lis = []
        while node != None:
            lis.append(node.val)
            node = node.next
        return lis

    def delete(self, data):
        node = self.head
        prev_node = self.head
        if not self.find(data):
            return
        elif self.head.val == data:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            while node:
                if node.val == data:
                    prev_node.next = node.next
                    break
                prev_node = node
                node = node.next

    def find(self, data):
        node = self.head
        while node:
            if node.val == data:
                return True
            node = node.next
        return False


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [None] * bucket_count

    def _hash_func(self, string):
        hashed_val = 0
        for index, char in enumerate(string):
            hashed_val += ord(char) * (self._multiplier ** index)
        return (((hashed_val % self._prime) + self._prime) % self._prime) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            #             print(f'checking index {query.ind}')
            ilist = self.elems[query.ind]
            if ilist:
                return self.write_chain(ilist.traverse())
            else:
                print('')
        else:
            index = self._hash_func(query.s)
            #             print(f'index = {index}')

            if query.type == 'find':
                #                 print(f'finding index = {index}')
                ll = self.elems[index]
                isFound = False
                if ll:
                    isFound = ll.find(query.s)
                self.write_search_result(isFound)
            elif query.type == 'add':
                #                 print(f'adding to index{index}; Val at index = {self.elems[index]}')
                if not self.elems[index]:
                    #                     print('made a linkedlist')
                    self.elems[index] = LinkedList()
                #                     print(f'adding to index = {index}')
                if not self.elems[index].find(query.s):
                    self.elems[index].insert_at_head(query.s)
            else:
                ll = self.elems[index]
                if ll:
                    if self.elems[index].find(query.s):
                        #                     print(f'Before Deleting : {self.elems[index].traverse()}')
                        self.elems[index].delete(query.s)

    #                     print(f'After Deleting : {self.elems[index].traverse()}')

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
