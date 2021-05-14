#python3
import math
from sys import stdin

class binary_max_heap():

    def __init__(self,array, maxSize):
        self.H = array
        self.Build_BMH()

        self.maxSize = maxSize

    def Build_BMH(self):
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

        while i > 0 and self.H[i] > self.H[self.parent(i)] :
            swap = self.H[i]
            self.H[i] = self.H[self.parent(i)]
            self.H[self.parent(i)] = swap
            i = self.parent(i)

    def siftDown(self,i):
        maxIndex = i

        l = self.leftChild(i)
        if l < len(self.H) and self.H[maxIndex] < self.H[l]:
            maxIndex = l

        r = self.rightChild(i)
        if r < len(self.H) and self.H[maxIndex] < self.H[r]:
            maxIndex = r

        if i != maxIndex:
            swap = self.H[i]
            self.H[i] = self.H[maxIndex]
            self.H[maxIndex] = swap
            self.siftDown(maxIndex)


    def insert(self,num):

        if len(self.H) < self.maxSize:
            self.H.append(num)

            self.siftUp(len(self.H)-1)

        else:
            return 'Heap Full!'

    def ExtractMax(self):
        if len(self.H) > 1:
            result = self.H[0]
            self.H[0] = self.H.pop()
            self.siftDown(0)
            return result
        elif len(self.H) == 1:
            result = self.H.pop()
            return result
        else:
            pass

    def getMax(self):
        return self.H[0]

    def remove(self,i):
        self.H[i] = math.inf
        self.siftUp(i)
        self.ExtractMax()

    def ChangePriority(self,i,p):
        old_p = self.H[i]
        self.H[i] = p
        if old_p < p:
            siftUp(i)
        else:
            siftDown(i)

    def PrintTree(self):
        pass


def max_sliding_window(m, nums):
    window = binary_max_heap(nums[:m:], m)
    result = []

    for i in range(len(nums) - m + 1):
        result.append(window.getMax())
        removable = window.H.index(nums[i])
        window.remove(removable)
        if i < len(nums)-m:
            window.insert(nums[m+i])

    return result

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    #data = list(map(int, input().split()))
    n = data[0]
    nums = data[1:len(data) - 1:]
    m = data[-1]

    result = max_sliding_window(m, nums)
    for num in result:
        print (num, end=" ")
