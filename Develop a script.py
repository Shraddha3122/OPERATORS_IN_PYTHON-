
numbers = [10, 20, 30, 40, 50, 60]


value = int(input("Enter a number to check: "))

if value in numbers:
    print(f"The number {value} exists in the list.")
else:
    print(f"The number {value} does not exist in the list.")
