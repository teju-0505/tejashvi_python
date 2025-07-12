def display_welcome():
    print("Welcome to the Pattern and Number Analysis Program!")
    print("Features:")
    print("1. Pattern Generation (Triangle, Pyramid, Diamond)")
    print("2. Number Analysis (Odd/Even and Sum)")
    print("3. Exit")


def get_positive_int(prompt):
    while True:
        try:
            value = int(prompt)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def pattern_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)


def pattern_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))


def pattern_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))


def pattern_generation():
    print("\nPattern Options: triangle, pyramid, diamond")
    pattern_type = input("Enter pattern type: ").lower()
    rows = get_positive_int("Enter number of rows: ")

    print("\nGenerated Pattern:")
    if pattern_type == "triangle":
        pattern_triangle(rows)
    elif pattern_type == "pyramid":
        pattern_pyramid(rows)
    elif pattern_type == "diamond":
        pattern_diamond(rows)
    else:
        print("Invalid pattern type!")


def number_analysis():
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        if end < start:
            print("End of range must be greater than start.")
            return

        print("\nOdd Numbers:")
        print([num for num in range(start, end + 1) if num % 2 != 0])
        print("Even Numbers:")
        print([num for num in range(start, end + 1) if num % 2 == 0])
        print("Sum of numbers in range:", sum(range(start, end + 1)))
    except ValueError:
        print("Invalid input. Please enter integers only.")


def main():
    display_welcome()
    while True:
        print("\nMain Menu:")
        print("1. Pattern Generation")
        print("2. Number Analysis")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            pattern_generation()
        elif choice == '2':
            number_analysis()
        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
