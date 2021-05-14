class Tree():
    def __init__(self,name, value, parent = None, child = None):

        self.name = name
        self.value = value
        self.child = []
        self.parent = parent
        self.height = 1

        if self.parent != None:
            self.parent.child.append(self)
            self.height = self.parent.height + 1

    def __str__(self):
        if (self.parent != None):
            string = f'Name = {self.name} \nValue = {self.value} \nParent = {self.parent.name} \nHeight = {self.height}'
        else:
            string = f'Name = {self.name}, \nValue = {self.value}, \nParent = None \nHeight = {self.height}'

        string = string + f' \nChildren of {self.name} -'

        if self.child == []:
            string = string + ' None'
        else:
            for children in self.child:
                string = string + f' {children.name},'
        string = string + '\n'
        return string

def tree_making(numlist):
    NodeList = []
    for index in range(len(numlist)):
        NodeList.append(Tree(f'Node_{index}', index, None))

    for index in range(len(NodeList)):
        if numlist[index] != -1:
            NodeList[index].parent = NodeList[numlist[index]]
            NodeList[numlist[index]].child.append(NodeList[index])

    return NodeList

def tree_height(numlist):
    NodeList = tree_making(numlist)
    for Node in NodeList:
        if Node.child == []:
            Node.height = 1
            while Node.parent != None:
                if Node.parent.height < Node.height + 1:
                    Node.parent.height = Node.height + 1
                    Node = Node.parent
                else:
                    break
    height = NodeList[numlist.index(-1)].height

    return height

if __name__ == '__main__':
    n = input()
    numlist = list(map(int,input().split()))
    print(tree_height(numlist))
