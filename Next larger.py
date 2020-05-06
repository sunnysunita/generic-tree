class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
list0 = []
def nextLargest(root, n):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return None

    if root.data > n:
        list0.append(root.data)

    for child in root.children:
        nextLargest(child, n)
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
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
nextLargest(tree, n)
print(min(list0))
