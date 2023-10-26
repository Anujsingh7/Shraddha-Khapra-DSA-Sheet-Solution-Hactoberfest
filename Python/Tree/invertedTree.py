class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def invert_tree(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)
    return node

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def build_tree():
    value = input("Enter node value (type 'exit' to stop): ")
    if value == 'exit':
        return None
    left_child = build_tree()
    right_child = build_tree()
    return TreeNode(value, left_child, right_child)

if __name__ == "__main__":
    print("Building the tree (input left child, then right child for each node):")
    tree = build_tree()

    print("\nOriginal Tree:")
    print_tree(tree)
    
    invert_tree(tree)
    print("\nInverted Tree:")
    print_tree(tree)
