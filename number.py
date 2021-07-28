
# Object that stores a value and decides if the value should be a float or
# an int
#
# val     => stores a float or int value

class Number():
    def __init__(self, x):
        try:
            self.val = int(x)
        except:
            self.val = float(x)

    # Useful for debugging code and determining order of operations
    def print(self):
        print(self.val, end = "")

    # Returns the stored value
    def eval(self):
        return self.val