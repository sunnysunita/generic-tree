class GenericTree:
    def __init__(self, data):
        self.data = data
        self.children = []

def generic_tree():
    root_data = int(input("Enter the root data: "))

    # edge case only
    if root_data == -1:
        return None

    root = GenericTree(root_data)
    num_children = int(input("Enter the number of children of "+str(root_data)+": "))
    for i in range(num_children):
        root.children.append(generic_tree())
    return root

root = generic_tree()
print(root.data)
print(root.children)
