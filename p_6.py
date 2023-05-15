class Student:
    def __init__(self, rollNumber, name):
        self.rollNumber = rollNumber
        self.name = name

class Exam(Student):
    def __init__(self, rollNumber, name, marks):
        super().__init__(rollNumber, name)
        self.marks = marks
    
class Result(Exam):
    def __init__(self, rollNumber, name, marks):
        super().__init__(rollNumber, name, marks)
        self.totalMarks = sum(marks)
    
    def displayResult(self):
        print("Roll Number:", self.rollNumber)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total Marks:", self.totalMarks)

# Interactive Program
rollNumber = input("Enter Roll Number: ")
name = input("Enter Name: ")
marks = []

for i in range(6):
    mark = int(input("Enter Marks for Subject {}: ".format(i+1)))
    marks.append(mark)

result = Result(rollNumber, name, marks)
result.displayResult()
