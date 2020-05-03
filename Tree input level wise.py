from queue import Queue
class GenericTree:
    def __init__(self, data):
        self.data = data
        self.children = []

def create_tree_levewise():
    root_data = int(input("Enter the root data: "))
    if root_data == -1:
        return None
    root = GenericTree(root_data)
    q = Queue()
    q.put(root)
    while q.empty() is False:
        curr = q.get()
        print("Enter the number of children", curr.data, ":")
        num_children = int(input())
        for i in range(num_children):
            child_data = int(input("Enter the child node value: "))
            child_node = GenericTree(child_data)
            root.children.append(child_node)
            q.put(child_node)
    return root


def print_generic_tree_detailed(root):
    if root is None:
        return None
    print(root.data, end=":")
    for e in root.children:
        print(e.data, end=",")
    print()
    for e in root.children:
        print_generic_tree_detailed(e)


root = create_tree_levewise()
print_generic_tree_detailed(root)
