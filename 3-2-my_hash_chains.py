#python3
from sys import stdin

def PolyHash(prime, x, m, S):
    h = 0
    for i in range(len(S))[::-1]:
        h = (h*x + ord(S[i])) % prime
    h = h % m

    return h

def Chaining_Hash(m, n, ops, strings):
    prime = 1000000007
    x = 263
    answer = []
    chains = [None]*m
    i = 0

    while i < len(ops):
        if ops[i] == 'add':
            h = PolyHash(prime, x, m, strings[i])
            if chains[h] == None:
                chains[h] = []
                chains[h].append(strings[i])
            else:
                if strings[i] in chains[h]:
                    pass
                else:
                    chains[h].append(strings[i])

        if ops[i] == 'del':
            h = PolyHash(prime, x, m, strings[i])

            if chains[h] == None:
                pass
            else:
                if strings[i] in chains[h]:
                    chains[h].pop(chains[h].index(strings[i]))
                else:
                    pass

        if ops[i] == 'find':
            h = PolyHash(prime, x, m, strings[i])
            if chains[h] == None:
                answer.append('no')
            elif strings[i] in chains[h]:
                answer.append('yes')
            else:
                answer.append('no')

        if ops[i] == 'check':
            strings[i] = int(strings[i])

            if chains[strings[i]] == None:
                answer.append('')
            else:
                answer.append(chains[strings[i]][::-1])

        i += 1

    return answer

if __name__ == '__main__':
    data = list(map(str, stdin.read().split()))
    #data = list(map(str, input().split()))
    m = int(data[0])
    n = int(data[1])
    ops = data[2::2]
    strings = data[3::2]
    result = Chaining_Hash(m, n, ops, strings)

    for item in result:
        if type(item) == str:
            print(item)
        elif type(item) == list:
            print(" ".join(x for x in item))
