from add import Add
from subtract import Subtract
from mult import Mult
from div import Div
from negate import Negate
from number import Number
import tokenize
from io import StringIO

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
                
                #print("+")
                
                self.scanToken()
                b = self.parseT()
                a = Add(a,b)
            elif self.nextToken == "-":
                
                #print("-")
                
                self.scanToken()
                b = self.parseT()
                a = Subtract(a,b)
            else:
                return a

    def parseT(self):
        a = self.parseF()

        while True:
            if self.nextToken == "*":
                
                #print("*")
                
                self.scanToken()
                b = self.parseT()
                a = Mult(a,b)
            elif self.nextToken == "/":
                
                #print("/")
                
                self.scanToken()
                b = self.parseT()
                a = Div(a,b)
            else:
                return a

    def parseF(self):
        if self.nextToken.replace(".","").isnumeric():
            
            #print(self.nextToken)

            num = Number(self.nextToken)
            self.scanToken()
            return num
        elif self.nextToken == "(":
            
            #print("(")
            
            self.scanToken()
            a = self.parseE()

            if a == None:
                return None
            
            if self.nextToken == ")":
                
                #print(")")
                
                self.scanToken()
                return a
            else:
                return None
        elif self.nextToken == "-":
            
            #print("-")
            
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


