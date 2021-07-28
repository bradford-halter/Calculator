
# Object that stores a value and decides if the value should be a float or an int
#
# val     => stores a float or int value
#
# print() => Useful for debugging code and determining order of operations
# eval()  => Returns val

class Number():
    def __init__(self, x):
        try:
            self.val = int(x)
        except:
            self.val = float(x)

    def print(self):
        print(self.val, end = "")

    def eval(self):
        return self.val