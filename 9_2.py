# Open the files
student_file = open("student.txt", "r")
marks_file = open("marks.txt", "r")

# Iterate through the lines in both files
for student, marks in zip(student_file, marks_file):
    # Remove the newline character and print the student name and marks
    print("Student:", student.strip(), "Marks:", marks.strip())

# Close the files
student_file.close()
marks_file.close()
