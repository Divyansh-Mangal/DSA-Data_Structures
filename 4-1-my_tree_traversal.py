#python3
#Pre-order, Post-order, in_order
from sys import stdin

class TreeNode():
    def __init__(self, name, value, parent = None, left = None, right = None):
        self.name = name
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        string = f' name = {self.name}'
        string += f' value = {self.value}'
        if self.parent != None:
            string += f' parent = {self.parent.name}'
        else:
            string += f' parent = {None}'

        if self.left != None:
            string += f' left = {self.left.name}'
        else:
            string += f' left = {None}'

        if self.right != None:
            string += f' right = {self.right.name}'
        else:
            string += f' right = {None}'

        return string


def inOrder(N, InOrder = []):

    if N == None:
        return

    inOrder(N.left, InOrder)
    InOrder.append(N.value)
    inOrder(N.right, InOrder)

    return InOrder

def preOrder(N, PreOrder = []):

    if N == None:
        return

    PreOrder.append(N.value)
    preOrder(N.left, PreOrder)
    preOrder(N.right, PreOrder)

    return PreOrder

def postOrder(N, PostOrder = []):

    if N == None:
        return

    postOrder(N.left, PostOrder)
    postOrder(N.right, PostOrder)
    PostOrder.append(N.value)

    return PostOrder


def TreeOrder(n, values, lefts, rights):
    NodeList = []
    for i in range(n):

        NodeList.append(TreeNode(i, values[i] , left = lefts[i],right =  rights[i]))

    for N in NodeList:
        if N.left != -1:
            N.left = NodeList[N.left]
            N.left.parent = N
        else:
            N.left = None

        if N.right != -1:
            N.right = NodeList[N.right]
            N.right.parent = N
        else:
            N.right = None

    return [inOrder(NodeList[0], []), preOrder(NodeList[0], []), postOrder(NodeList[0],[]) ]


if __name__ == '__main__':
    #data = list(map(int, stdin.read().split()))
    data = list(map(int, input().split()))
    n = data[0]
    NodeValue = data[1::3]
    NodeLeft = data[2::3]
    NodeRight = data[3::3]

    result = TreeOrder(n, NodeValue, NodeLeft, NodeRight)

    for i in result:
        for n in i:
            print(n, end = " ")
        print('', end = "\n")
