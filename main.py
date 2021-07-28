from calc import Calc

# Runs the calculator by passing in the user input to a calculator object and
# attempting to print the evaluation of the input

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
            print(calc.eval())

    print("Have a good day!")

if __name__ == "__main__":
    main()