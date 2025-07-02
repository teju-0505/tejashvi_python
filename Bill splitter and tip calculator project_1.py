if True:
    print("\nwelcome to the Bill splitter App\n")

# Getting user input

number_of_people = int(input("Enter number of people: "))
total_bill = float(input("Enter total bill amount: "))
tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))

tip_amount = total_bill * (tip_percentage / 100)
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / number_of_people

print(f"\nTip_Amount: ₹{tip_amount:.2f}")
print(f"Total Bill (with Tip): ₹{total_with_tip:.2f}")
print(f"Each person should pay: ₹{amount_per_person:.2f}")

# Ask to contiune or exit
repeat = input("\nwould you like to calculate another bill? (yes/no): ").lower()
if repeat != 'yes':
  Break
