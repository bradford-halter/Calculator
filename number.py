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