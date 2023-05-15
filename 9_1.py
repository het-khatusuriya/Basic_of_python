# Open the files
odd_file = open("odd.txt", "w")
even_file = open("even.txt", "w")

# Iterate through numbers from 1 to 10
for i in range(1, 11):
    # Check if the number is even or odd
    if i % 2 == 0:
        even_file.write(str(i) + "\n")
    else:
        odd_file.write(str(i) + "\n")

# Close the files
odd_file.close()
even_file.close()
