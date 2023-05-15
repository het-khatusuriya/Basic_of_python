# Create a file
file = open("example.txt", "w")

# Write some text to the file
file.write("Hello, World!\n")

# Close the file
file.close()

# Open the file again
file = open("example.txt", "r")

# Read the text from the file and print it
text = file.read()
print(text)

# Close the file
file.close()
