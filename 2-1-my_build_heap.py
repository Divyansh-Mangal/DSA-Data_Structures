#python3
import math
from sys import stdin

class binary_min_heap():

    def __init__(self,array, maxSize):
        self.H = array
        self.swap_num = 0
        self.swaps = []

        self.Build_BmH()
        self.maxSize = maxSize


    def Build_BmH(self):
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
        if l < len(self.H) and self.H[maxIndex] > self.H[l]:
            maxIndex = l

        r = self.rightChild(i)
        if r < len(self.H) and self.H[maxIndex] > self.H[r]:
            maxIndex = r

        if i != maxIndex:
            swap = self.H[i]
            self.H[i] = self.H[maxIndex]
            self.H[maxIndex] = swap
            self.swaps.append((i, maxIndex))
            self.swap_num += 1
            self.siftDown(maxIndex)

def build_min_heap(heap_array,n):
    BmH = binary_min_heap(heap_array, n)
    return BmH.swap_num, BmH.swaps

if __name__ == '__main__':
    #data = list(map(int,input().split()))
    data = list(map(int,stdin.read().split()))
    n = data[0]
    heap_array = data[1::]
    swap_num, swaps = build_min_heap(heap_array,n)

    print(swap_num)
    for i,j in swaps:
        print(i,j)
