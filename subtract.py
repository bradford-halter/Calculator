from treenode import TreeNode

# TreeNode Object that stores a left TreeNode, a right TreeNode, and 
# implicitly subtracts the left and right TreeNodes together
#
# left, right => TreeNode which can either be a new expression or a number

class Subtract(TreeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    # Useful for debugging code and determining order of operations
    def print(self):
        print("(", end ="")
        self.left.print()
        print("-", end ="")
        self.right.print()
        print(")", end ="")

    # Returns the difference of left and right
    def eval(self):
        return self.left.eval() - self.right.eval()