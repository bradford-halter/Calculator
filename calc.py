from add import Add
from subtract import Subtract
from multiply import Multiply
from divide import Divide
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

class Calc:
    def __init__(self, inputStr):
        self.inputTokens = []

        if len(inputStr) > 0:
            for token in tokenize.generate_tokens(
                StringIO(inputStr).readline):
                self.inputTokens.append(token)

            if len(self.inputTokens) > 0:
                self.nextToken = self.inputTokens.pop(0).string
                self.resultTree = self.parseExpression()
            else:
                self.nextToken = None
                self.resultTree = None

    # Parses the next expression from the input. This also creates the addition 
    # and subtraction objects since it has lower precedence than parseTerm()
    # and parseFactor()
    def parseExpression(self):
        a = self.parseTerm()

        while True:
            if self.nextToken == "+":
                self.scanToken()
                b = self.parseTerm()
                a = Add(a,b)
            elif self.nextToken == "-":
                self.scanToken()
                b = self.parseTerm()
                a = Subtract(a,b)
            else:
                return a

    # Parses the next term from the input. This also creates the 
    # multiplication and division objects since it has lower precedence 
    # than parseFactor()
    def parseTerm(self):
        a = self.parseFactor()

        while True:
            if self.nextToken == "*":
                self.scanToken()
                b = self.parseTerm()
                a = Multiply(a,b)
            elif self.nextToken == "/":
                self.scanToken()
                b = self.parseTerm()
                a = Divide(a,b)
            else:
                return a

    # Parses the next factor from the input. This also deals with parentheses
    # and creates the negation objects since it has the highest precendence
    def parseFactor(self):
        if self.nextToken.replace(".","").isnumeric():
            num = Number(self.nextToken)
            self.scanToken()
            return num
        elif self.nextToken == "(":
            self.scanToken()
            a = self.parseExpression()

            if a == None:
                return None
            
            if self.nextToken == ")":
                self.scanToken()
                return a
            else:
                return None
        elif self.nextToken == "-":
            self.scanToken()
            return Negate(self.parseFactor())
        else:
            return None

    # Useful for debugging code and determining order of operations
    def print(self):
        try:
            self.resultTree.print()
            print()
        except:
            print("Invalid Input")

    # Returns the value of the input expression
    def eval(self):
        try:
            return self.resultTree.eval()
        except:
            print("Invalid Input")
        

    # Pops the first token from inputTokens and assigns the string value to 
    # nextToken
    def scanToken(self):
        if len(self.inputTokens) > 0:
            self.nextToken = self.inputTokens.pop(0).string
        else:
            self.nextToken = None


