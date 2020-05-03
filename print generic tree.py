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

def print_generic_tree(root):
    # edge case only
    if root is None:
        return
    print(root.data)
    for e in root.children:
        print_generic_tree(e)

def print_generic_tree_detailed(root):
    if root is None:
        return None
    print(root.data, end=":")
    for e in root.children:
        print(e.data, end=",")
    print()
    for e in root.children:
        print_generic_tree_detailed(e)


root = generic_tree()
print_generic_tree(root)
print_generic_tree_detailed(root)

