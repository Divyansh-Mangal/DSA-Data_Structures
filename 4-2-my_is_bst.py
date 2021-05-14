# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        data = list(map(int, sys.stdin.read().split()))
        #data = list(map(int, input().split()))
        self.n = data[0]
        if self.n > 0:
            self.key = data[1::3]
            self.left = data[2::3]
            self.right = data[3::3]

            for i in range(self.n):
                if self.left[i] == -1:
                    self.left[i] = None

                if self.right[i] == -1:
                    self.right[i] = None


def inOrder(tree, i, result):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i == None:
        return

    inOrder(tree, tree.left[i], result)
    result.append(tree.key[i])
    inOrder(tree, tree.right[i], result)

    return result


def main():
    tree = TreeOrders()
    tree.read()
    it_is = 'CORRECT'

    if tree.n > 0:
        in_order = inOrder(tree, 0, [])
        for i in range(len(in_order)-1):
            if in_order[i] >= in_order[i+1]:
                it_is = 'INCORRECT'
                break
    print(it_is)

threading.Thread(target=main).start()
