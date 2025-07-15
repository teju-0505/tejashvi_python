def main_menu():
    print("\nWelcome to the Data Analyzer and Transformer Program\n")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

def input_data():
    data = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
    print("\nData has been stored successfully!")
    return data

def display_summary(data):
    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def filter_data(data):
    threshold = int(input("Enter threshold value: "))
    filtered = list(filter(lambda x: x > threshold, data))
    print("Filtered Data (greater than threshold):", filtered)

def sort_data(data):
    sorted_data = sorted(data)
    print("Sorted Data:", sorted_data)

def dataset_stats(data):
    avg = sum(data) / len(data)
    med = sorted(data)[len(data) // 2]
    return avg, med

# Main loop
data = []
while True:
    main_menu()
    choice = input("Please enter your choice: ")
    
    if choice == '1':
        print("\nStep 1: Input Data")
        data = input_data()
    elif choice == '2':
        if data:
            print("\nStep 2: Display Data Summary (Built-in Functions)")
            display_summary(data)
        else:
            print("Please input data first.")
    elif choice == '3':
        n = int(input("Enter a number to calculate factorial: "))
        print(f"Factorial of {n} is {factorial(n)}")
    elif choice == '4':
        if data:
            filter_data(data)
        else:
            print("Please input data first.")
    elif choice == '5':
        if data:
            sort_data(data)
        else:
            print("Please input data first.")
    elif choice == '6':
        if data:
            avg, med = dataset_stats(data)
            print(f"Average: {avg}, Median: {med}")
        else:
            print("Please input data first.")
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
