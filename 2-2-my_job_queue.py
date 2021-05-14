#python3
#Implementing parallel processing
from sys import stdin


import math
class binary_min_heap_pp():

    def __init__(self,array, maxSize):
        self.H = array

        self.Build_min_heap()

        self.maxSize = maxSize

        self.fill_in = 0

    def Build_min_heap(self):
        n = len(self.H)
        i = math.floor(n/2)
        while i >= 0:
            self.siftDown(i)
            i -= 1

    def parent(self,i):
        return math.floor((i-1)/2)

    def leftChild(self,i):
        return 2*(i) + 1

    def rightChild(self,i):
        return 2*(i) + 2

    def siftUp(self,i):

        while i > 0 and self.H[i][0] < self.H[self.parent(i)][0] :
            swap = self.H[i]
            self.H[i] = self.H[self.parent(i)]
            self.H[self.parent(i)] = swap
            i = self.parent(i)


    def siftDown(self,i):
        maxIndex = i

        l = self.leftChild(i)
        r = self.rightChild(i)

        if l < len(self.H) and self.H[maxIndex][0] > self.H[l][0]:
            maxIndex = l

        if r < len(self.H) and self.H[maxIndex][0] > self.H[r][0]:
            maxIndex = r

        if l < len(self.H) and r < len(self.H) and self.H[l][0] == self.H[r][0]:
            if self.H[r][2] < self.H[l][2] and self.H[maxIndex][0] >= self.H[r][0]:
                    maxIndex = r

            elif self.H[l][2] < self.H[r][2] and self.H[maxIndex][0] >= self.H[l][0]:
                    maxIndex = l

        if i != maxIndex:
            swap = self.H[i]
            self.H[i] = self.H[maxIndex]
            self.H[maxIndex] = swap
            self.siftDown(maxIndex)


    def insert(self,value, time):

        if len(self.H) < self.maxSize:
            tup = (value + time, time, self.fill_in)
            self.H.append(tup)

            if self.fill_in < self.maxSize-1:
                self.fill_in += 1
            else:
                self.fill_in = 0

            self.siftUp(len(self.H)-1)

            return tup
        else:
            return 'Heap Full!'

    def ExtractMin(self):
        if len(self.H) > 1:
            result = self.H[0]

            self.H[0] = self.H.pop()
            self.siftDown(0)

            self.fill_in = result[2]

            return result
        elif len(self.H) == 1:
            result = self.H.pop()
            self.fill_in = result[2]
            return result
        else:
            pass


def parallel_processing(threads, tasks):
    ans_array = []
    chip = binary_min_heap_pp([], threads)
    pointer = 0
    time = 0

    while len(ans_array) < len(tasks):
        if len(chip.H) < threads:
            tup = chip.insert(tasks[pointer],time)
            ans_array.append((tup[2], time))
            pointer += 1

        elif len(chip.H) == threads:
            remove = chip.ExtractMin()
            time = remove[0]

    return ans_array


if __name__ == '__main__':
    #data = list(map(int, input().split()))
    data = list(map(int, stdin.read().split()))
    threads = data [0]
    thread_num = data[1]
    tasks = data[2::]
    answer = parallel_processing(threads, tasks)
    for thread, time in answer:
        print(thread, time)
