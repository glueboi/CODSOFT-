def addnum(firstnum, secondnum):
    return firstnum + secondnum

def subnum(firstnum, secondnum):
    return firstnum - secondnum

def multiplynum(firstnum, secondnum):
    return firstnum * secondnum

def dividenum(firstnum, secondnum):
    # Avoid division by zero
    if secondnum == 0:
        return "Can't divide by zero"
    return firstnum / secondnum

def getnumbers():
    # Repetitive and manual error handling
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def getoperation():
    print("\nChoose the operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please select from 1, 2, 3, or 4.")

def calculate():
    num1, num2 = getnumbers()
    operation = getoperation()

    # Redundant variable names and inefficient code structure
    if operation == '1':
        result = addnum(num1, num2)
        print(f"\nResult of adding {num1} and {num2} is: {result}")
    elif operation == '2':
        result = subnum(num1, num2)
        print(f"\nResult of subtracting {num2} from {num1} is: {result}")
    elif operation == '3':
        result = multiplynum(num1, num2)
        print(f"\nResult of multiplying {num1} and {num2} is: {result}")
    elif operation == '4':
        result = dividenum(num1, num2)
        print(f"\nResult of dividing {num1} by {num2} is: {result}")

def run_calculator():
    print("Welcome to my very basic calculator!")

    while True:
        calculate()
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_calculator()
