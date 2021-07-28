from add import Add
from subtract import Subtract
from mult import Mult
from div import Div
from negate import Negate
from number import Number
import tokenize
from io import StringIO


# Object that takes a string input, parses that input into tokens, and evaluates
# the representation of the input
#
# inputTokens => List that contains a tokenized version of the input
# nextToken   => Next unscanned token from the inputTokens List
# resultTree  => TreeNode Object that contains the root node of the expression
#
# parseE()    => Parses the next expression from the input. This also creates the
#                addition and subtraction objects since it has lower precedence than
#                parseT() and parseF()
# parseT()    => Parses the next term from the input. This also creates the multiplication
#                and division objects since it has lower precedence than parseF()
# parseF()    => Parses the next factor from the input. This also deals with parentheses
#                and creates the negation objects since it has the highest precendence
# print()     => Useful for debugging code and determining order of operations
# eval()      => Returns the sum of left and right
# scanToken() => Pops the first token from inputTokens and assigns the string value to
#                nextToken

class Calc:
    def __init__(self, inputStr):
        self.inputTokens = []

        if len(inputStr) > 0:
            for token in tokenize.generate_tokens(StringIO(inputStr).readline):
                self.inputTokens.append(token)

            if len(self.inputTokens) > 0:
                self.nextToken = self.inputTokens.pop(0).string
                self.resultTree = self.parseE()
            else:
                self.nextToken = None
                self.resultTree = None

    def parseE(self):
        a = self.parseT()

        while True:
            if self.nextToken == "+":
                self.scanToken()
                b = self.parseT()
                a = Add(a,b)
            elif self.nextToken == "-":
                self.scanToken()
                b = self.parseT()
                a = Subtract(a,b)
            else:
                return a

    def parseT(self):
        a = self.parseF()

        while True:
            if self.nextToken == "*":
                self.scanToken()
                b = self.parseT()
                a = Mult(a,b)
            elif self.nextToken == "/":
                self.scanToken()
                b = self.parseT()
                a = Div(a,b)
            else:
                return a

    def parseF(self):
        if self.nextToken.replace(".","").isnumeric():
            num = Number(self.nextToken)
            self.scanToken()
            return num
        elif self.nextToken == "(":
            self.scanToken()
            a = self.parseE()

            if a == None:
                return None
            
            if self.nextToken == ")":
                self.scanToken()
                return a
            else:
                return None
        elif self.nextToken == "-":
            self.scanToken()
            return Negate(self.parseF())
        else:
            return None

    def print(self):
        try:
            self.resultTree.print()
            print()
        except:
            print("Invalid Input")

    def eval(self):
        try:
            print(self.resultTree.eval())
        except:
            print("Invalid Input")
        

    def scanToken(self):
        if len(self.inputTokens) > 0:
            self.nextToken = self.inputTokens.pop(0).string
        else:
            self.nextToken = None


