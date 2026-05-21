print("🔥 Welcome to Archana Calculator 🔥")

while True:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))

    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    choice = input("Enter the choice: ")

    if choice == "1":
        print("Result:", n1 + n2)
    elif choice == "2":
        print("Result:", n1 - n2)
    elif choice == "3":
        print("Result:", n1 * n2)
    elif choice == "4":
        if n2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", n1 / n2)
    else:
        print("Invalid choice. Please choose 1 to 4.")

    again = input("Do you want to continue? (y/n): ").strip().lower()
    if again != "y":
        print("Thank you for using Archana Calculator!")
        break
