# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start a counter for the rows
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in one row
    for col in range(size):
        print("*", end="")  # Print stars side by side
    print()  # Move to the next line after one row
    row += 1  # Go to the next row
