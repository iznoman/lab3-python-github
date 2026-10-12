# Making Python calculator easier to understand and read

# Function to get two numbers
def getnumbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    while True:
        try:
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    return num1, num2


# Function for addition
def addition():
    x, y = getnumbers()
    print("Sum =", x + y)


# Function for subtraction
def subtraction():
    x, y = getnumbers()
    print("Difference =", x - y)


# Function for multiplication
def multiplication():
    x, y = getnumbers()
    print("Product =", x * y)


# Function for division
def division():
    x, y = getnumbers()

    if y != 0:
        print("Division =", x / y)
    else:
        print("Error! Division by zero is not allowed.")


# Function to check even or odd
def even_odd():
    x, y = getnumbers()

    print(x, "is Even" if x % 2 == 0 else "is Odd")
    print(y, "is Even" if y % 2 == 0 else "is Odd")


# Function for percentage
def percentage():
    x, y = getnumbers()

    if y != 0:
        print(f"{x} is {x / y * 100:.2f}% of {y}")
    else:
        print("Error! Cannot calculate a percentage with zero as the denominator.")


# Main program
while True:
    print("\n===== Calculator Menu =====")
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Even or Odd")
    print("6. Percentage")

    try:
        choice = int(input("Please select an option (0-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 6.")
        continue

    if choice == 0:
        print("Thank you for using the calculator. Goodbye!")
        break

    elif choice == 1:
        addition()

    elif choice == 2:
        subtraction()

    elif choice == 3:
        multiplication()

    elif choice == 4:
        division()

    elif choice == 5:
        even_odd()

    elif choice == 6:
        percentage()

    else:
        print("Invalid choice! Please select an option from 0 to 6.")
