from queue import Queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(root):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return None
    q = Queue()
    q.put(root)
    while q.empty() is False:
        curr = q.get()
        print(str(curr.data), end=":")
        for child in curr.children:
            if curr.children.index(child) == len(curr.children)-1:
                print(str(child.data), end="")
            else:
                print(str(child.data), end=",")
            q.put(child)
        print()



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
