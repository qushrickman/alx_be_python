# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop to print asterisks in a row
    for col in range(size):
        print("*", end="")  # Print without new line
    print()  # Move to the next line after each row
    row += 1
