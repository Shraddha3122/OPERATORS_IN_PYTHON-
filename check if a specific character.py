
input_string = input("Enter a string: ")        # Input: a string and a character to check
character = input("Enter the character to search for: ")


if character in input_string:       # Check if the character exists in the string
    print(f"The character '{character}' exists in the string.")
else:
    print(f"The character '{character}' does not exist in the string.")

