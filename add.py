from treenode import TreeNode

# TreeNode Object that stores a left TreeNode, a right TreeNode, and 
# implicitly adds the left and right TreeNodes together
#
# left, right => TreeNode which can either be a new expression or a number

class Add(TreeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    # Useful for debugging code and determining order of operations
    def print(self):
        print("(", end ="")
        self.left.print()
        print("+", end ="")
        self.right.print()
        print(")", end ="")

    # Returns the sum of left and right
    def eval(self):
        return self.left.eval() + self.right.eval()