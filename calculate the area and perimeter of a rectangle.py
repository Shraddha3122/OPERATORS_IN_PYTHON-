
def calculate_area(length, width):     # Function to calculate the area of a rectangle
    return length * width
def calculate_perimeter(length, width):     # Function to calculate the perimeter of a rectangle
    return 2 * (length + width)

length = float(input("Enter the length of the rectangle: "))        # Input: length and width of the rectangle
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)


print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")

