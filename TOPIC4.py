# Binary Tree to Manage Fixed Routes
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return BinaryTreeNode(data)
        if not root.left:
            root.left = self.insert(root.left, data)
        elif not root.right:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" -> ")
            self.inorder(root.right)

print("\n=== Binary Tree ===")
bt = BinaryTree()
root = None
for data in ["Kigali_Muhanga", "Kigali_Nyanza", "Kigali_Huye"]:
    root = bt.insert(root, data)
print("Binary Tree Inorder Traversal:")
bt.inorder(root)