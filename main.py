from calc import Calc

def main():
    print("Welcome to simple calculator")

    while True:
        
        
        print("Please input an expression to compute or q to quit")

        expression = input()
        
        if expression.__eq__("q"):
            break
        else:
            calc = Calc(expression.replace(" ", ""))

            #calc.print()
            calc.eval()

    print("Have a good day!")

if __name__ == "__main__":
    main()