from sys import stdin

class stack():
    def __init__(self):
        self.s = []
        self.max = []

    def push(self, num):
        self.s.append(num)
        if self.max != []:
            if self.max[-1] < num:
                self.max.append(num)
            else:
                self.max.append(self.max[-1])
        else:
            self.max.append(num)

    def pop(self):
        self.s.pop()
        self.max.pop()

    def __str__(self):
        return f'{self.s} with {self.max} as auxilliary max_stack'

    def maximum(self):
        return self.max[-1]

def extended_stack(n, operations):
    stk = stack()
    maximums = []
    index = 0

    while index < len(operations):
        if operations[index] == 'push':
            index += 1
            stk.push(int(operations[index]))
        elif operations[index] == 'pop':
            stk.pop()
        elif operations[index] == 'max':
            maximums.append(stk.maximum())

        index += 1

    return maximums

if __name__ == '__main__':
    data = list(map(str, stdin.read().split()))
    #data = list(map(str, input().split()))
    n = data[0]
    operations = data[1::]
    #print(n, operations)

    for _ in extended_stack(n, operations):
        print(_)
