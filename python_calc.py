#improve the meassages
def getnumbers():
    while True:
        try:
            num1 = int(input("Enter First number: "))
            break
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            num2 = int(input("Enter Second number: "))
            break
        except ValueError:
            print("Please enter a valid number")

    return num1, num2


while True:
    print("\nEnter a choice")
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Even OR Odd")
    print("6. Percentage")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice")
        continue

    if choice == 0:
        print("Goodbye!")
        break

    elif choice in (1, 2, 3, 4, 5, 6):
        x, y = getnumbers()

        if choice == 1:
            print("Sum =", x + y)

        elif choice == 2:
            print("Difference =", x - y)

        elif choice == 3:
            print("Product =", x * y)

        elif choice == 4:
            if y != 0:
                print("Division =", x / y)
            else:
                print("Cannot divide by zero")

        elif choice == 5:
            print(x, "is Even" if x % 2 == 0 else "is Odd")
            print(y, "is Even" if y % 2 == 0 else "is Odd")

        elif choice == 6:
            if y != 0:
                print(f"{x} is {x / y * 100:.2f}% of {y}")
            else:
                print("Cannot calculate percentage with zero as denominator")

    else:
        print("Invalid choice. Please select 0-6.")
