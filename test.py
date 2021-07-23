from add import Add
from integer import Integer
from negate import Negate
from mult import Mult

def test():
    #tn1 = TreeNode(5)
    int1 = Integer(1)
    int2 = Integer(5)
    int3 = Integer(2)
    a1 = Add()
    
    a1.left = int1
    a1.right = int2

    n1 = Negate()
    n1.left = a1

    m1 = Mult()
    m1.left = n1
    m1.right = int3


    
    #int1.print()
    #int2.print()
    #a1.left.print()
    #a1.right.print()
    m1.print()
    print()
    print(m1.eval())

def main():
    test()

if __name__ == "__main__":
    main()