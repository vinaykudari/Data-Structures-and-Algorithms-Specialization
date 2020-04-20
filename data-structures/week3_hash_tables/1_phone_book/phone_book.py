# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    phonebook = [None]*10**7

    for query in queries:
        if query.type == 'add':
            phonebook[query.number] = query.name
        elif query.type == 'del':
            phonebook[query.number] = None
        elif query.type == 'find':
            name = phonebook[query.number]
            if name:
                result.append(name)
            else:
                result.append("not found")
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

