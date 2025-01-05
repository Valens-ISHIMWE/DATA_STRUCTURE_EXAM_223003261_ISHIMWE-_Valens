# Tree for Hierarchical Transport System
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)

print("\n=== Tree Hierarchy ===")
root_node = TreeNode("Transport System")
buses = TreeNode("Buses")
Rwanda_Air = TreeNode("Rwanda_Air")
buses.add_child(TreeNode("VOLCANO"))
buses.add_child(TreeNode("HORIZON"))
Rwanda_Air.add_child(TreeNode("Rwanda_Air A"))
root_node.add_child(buses)
root_node.add_child(Rwanda_Air)
root_node.display()