#python3

from sys import stdin

def Phone_book(ops):
    answer = []
    maxLen = max(len(op) for op in ops)

    Ph_Book = {}
    i = 0

    while i in range(len(ops)):
        if ops[i] == 'find':
            i += 1
            number = int(ops[i])

            hasKey = Ph_Book.get(number)
            if hasKey != None:
                answer.append(Ph_Book[number])
            else:
                answer.append('not found')

        elif ops[i] == 'del':
            i += 1
            number = int(ops[i])

            hasKey = Ph_Book.get(number)
            if hasKey != None:
                Ph_Book.pop(number)
            else:
                pass


        elif ops[i] == 'add':
            i += 1
            number = int(ops[i])
            i += 1
            name = ops[i]

            Ph_Book[number] = name

        i += 1

    return answer


if __name__ == '__main__':
    data = list(map(str, stdin.read().split()))
    #data = list(map(str, input().split()))
    n = data[0]
    ops = data[1::]

    answer = Phone_book(ops)
    for string in answer:
        print(string)
