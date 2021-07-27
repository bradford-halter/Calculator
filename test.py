from add import Add
from negate import Negate
from mult import Mult
from number import Number
import tokenize
from io import StringIO

def test():
    #tn1 = TreeNode(5)
    int1 = Number(1)
    int2 = Number(5)
    int3 = Number(2)
    a1 = Add(int1, int2)

    n1 = Negate(a1)

    m1 = Mult(n1, int3)
    
    #int1.print()
    #int2.print()
    #a1.left.print()
    #a1.right.print()
    #m1.print()
    #print()
    #print(m1.eval())

    #test = "helloooo  !"
    #print(test.replace(" ", ""))

    #digit = ['0','1','2','3','4','5','6','7','8','9']
    #test = "."
    #print(test in digit)

    test = input()

    testTokens = []
    
    for token in tokenize.generate_tokens(StringIO(test).readline):
        testTokens.append(token)

    while len(testTokens) > 0:
        print(testTokens.pop(0).string)


    #print(testTokens.pop(0).string)
    #print(testTokens.pop(0).string)
    #print(testTokens.pop(0).string)
    #print(testTokens.pop(0).string)
    #print(testTokens.pop(0).string)

    #test = "11"
    #try:
    #    test = int(test)
    #except:
    #    test = float(test)
    
    #print(test.replace(".", "").isnumeric())

    #test = []
    #print(test[0])



def main():
    test()

if __name__ == "__main__":
    main()