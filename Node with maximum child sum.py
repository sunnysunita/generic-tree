class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(root):
    # Return the node and its sum
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return None, None
    temp = root
    tempSum = root.data
    for child in root.children:
        tempSum = tempSum + child.data
    for child in root.children:
        sub_child, sub_sum = maxSumNode(child)
        if sub_sum > tempSum:
            temp = sub_child
            tempSum = sub_sum
    return temp, tempSum


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
temp, tempSum = maxSumNode(tree)
if temp is not None:
    print(temp.data)
