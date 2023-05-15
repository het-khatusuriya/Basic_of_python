# Open the file
file = open("triangle.txt", "w")

# Loop through the rows of the triangle
for i in range(1, 6):
    # Calculate the number of spaces and asterisks for this row
    spaces = " " * (5 - i)
    asterisks = "*" * (2 * i - 1)
    
    # Print the row to the console and write it to the file
    row = spaces + asterisks + spaces
    print(row)
    file.write(row + "\n")

# Close the file
file.close()
