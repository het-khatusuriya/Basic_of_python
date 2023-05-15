class Student1:
 def __init__(self,cgpa1):
   self.cgpa1=cgpa1
 def display(self):
   print("cgpa1:",self.cgpa1)
class Student2:
 def __init__(self,cgpa2):
   self.cgpa2=cgpa2
 def display(self):
   print("cgpa2:",self.cgpa2)
obj1=Student1(9)
obj2=Student2(10)
obj1.display()
obj2.display()
if(obj1.cgpa1<obj2.cgpa2):
 print("student2 is first")
else:
 print("student1 is first")
print("D22CE166")  
