from add import Add
from negate import Negate
from multiply import Multiply
from number import Number
import tokenize
from io import StringIO
from calc import Calc

def test():
    #int1 = Number(1)
    #int2 = Number(5)
    #int3 = Number(2)
    #a1 = Add(int1, int2)

    #n1 = Negate(a1)

    #m1 = Mult(n1, int3)
    
    #int1.print()
    #int2.print()
    #a1.left.print()
    #a1.right.print()
    #m1.print()
    #print()
    #print(m1.eval())

    #test = "helloooo  !"
    #print(test.replace(" ", ""))

    #test = "11"
    #try:
    #    test = int(test)
    #except:
    #    test = float(test)
    
    #print(test.replace(".", "").isnumeric())

    #test = []
    #print(test[0])

    tests = []
    tests.append("22")
    tests.append("2+2")
    tests.append("2-2")
    tests.append("2*2")
    tests.append("2/2")
    tests.append("(2)")
    tests.append("-2")
    tests.append("2+2*2")
    tests.append("3*(2+2)")
    tests.append("(2+4)/2")
    tests.append("")
    tests.append("())")
    tests.append("5**5")

    for test in tests:
        calc = Calc(test)
        print(calc.eval())
    
    #calc1 = Calc(test7)
    #print(calc1.eval() is "Invalid Input")
    #calc2 = Calc(test8)
    #print(calc2.eval() is "Invalid Input")



def main():
    test()

if __name__ == "__main__":
    main()