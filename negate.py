from treenode import TreeNode

# TreeNode Object that stores a left TreeNode and implicitly negates that 
# value. Note that there is no right TreeNode.
#
# left => TreeNode which can either be a new expression or a number

class Negate(TreeNode):
    def __init__(self, x):
        super().__init__(x, None)

    # Useful for debugging code and determining order of operations
    def print(self):
        print("(", end ="")
        print("-", end ="")
        self.left.print()
        print(")", end ="")

    # Returns the negation of left
    def eval(self):
        return -self.left.eval()