# python3

import sys, threading, math
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

            self.maximum = [None]*self.n
            self.minimum = [None]*self.n

            for i in range(self.n):
                if self.left[i] == -1:
                    self.left[i] = None

                if self.right[i] == -1:
                    self.right[i] = None


def inOrder(tree, i, result ,check):

    if i == None:
        return result , check

    result, check = inOrder(tree, tree.left[i], result, check)

    result.append(i)

    if tree.left[i] == None and tree.right[i] == None:
        tree.maximum[i] = tree.key[i]
        tree.minimum[i] = tree.key[i]

    elif tree.left[i] != None:
        if tree.maximum[tree.left[i]] >= tree.key[i]:
            check = False


    result, check = inOrder(tree, tree.right[i], result, check)

    if tree.right[i] != None:
        if tree.minimum[tree.right[i]] < tree.key[i]:
            check = False

    if tree.left[i] != None and tree.right[i] != None:
        tree.maximum[i] = max(tree.key[i], tree.maximum[tree.left[i]], tree.maximum[tree.right[i]])
    elif tree.left[i] != None and tree.right[i]== None:
        tree.maximum[i] = max(tree.key[i], tree.maximum[tree.left[i]])
    elif tree.left[i] == None and tree.right[i]!= None:
        tree.maximum[i] = max(tree.key[i], tree.maximum[tree.right[i]])
    elif tree.left[i] == None and tree.right[i]== None:
        tree.maximum[i] = tree.key[i]

    if tree.left[i] != None and tree.right[i] != None:
        tree.minimum[i] = min(tree.key[i], tree.minimum[tree.left[i]], tree.minimum[tree.right[i]])
    elif tree.left[i] != None and tree.right[i]== None:
        tree.minimum[i] = min(tree.key[i], tree.minimum[tree.left[i]])
    elif tree.left[i] == None and tree.right[i]!= None:
        tree.minimum[i] = min(tree.key[i], tree.minimum[tree.right[i]])
    elif tree.left[i] == None and tree.right[i]== None:
        tree.minimum[i] = tree.key[i]



    return result, check

def main():
    tree = TreeOrders()
    tree.read()

    if tree.n > 0:
        result, check = inOrder(tree, 0, [], True)

        if check:
            print('CORRECT')
        else:
            print('INCORRECT')
    else:
        print('CORRECT')


threading.Thread(target=main).start()
