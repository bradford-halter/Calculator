def main():
    
    print("Welcome to simple calculator")

    while True:
        print("Please input an expression to compute or q to quit")

        expression = input()
        
        print(expression)
        
        if expression.__eq__("q"):
            break

        

    print("Have a good day!")

if __name__ == "__main__":
    main()