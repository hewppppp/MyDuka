class Student:
    def __init__(self, name, age, student_no, course):
        self.name = name
        self.age = age
        self.student_no = student_no
        self.course = course

    def study(self):
        print(f"{self.name} studies")
    
    def enroll(self):
        print(f"{self.name} enrollments")
    
    def owes(self):
        print(f"{self.name} owes this fee balance")
    
    def sleeps(self,time):
        print(f"{self.name} sleeps at {time} ")
    
    def eats(self):
        print(f"{self.name} eats")

    def display_info(self):
        print("-----------------User Details--------------------")
        print(f"Name:{self.name} - Age: {self.age} - S-NO {self.student_no} - Course :{self.course}")
        print("--------------------------------------------------------------")

#object one
student1 = Student("Hope",19,"S345","Information Tech")  
print(type(student1)) 
print(student1.name) 
print(student1.age)
print(student1.course)
print(student1.student_no) 
student1.enroll()
student1.study()
student1.owes()
student1.sleeps("7pm")
student1.eats()
student1.display_info()
#obj 2
student2 =  Student("Nelly",19,"S349","Data Analytics")
print(type(student2)) 
print(student2.name) 
print(student2.age)
print(student2.course)
print(student2.student_no) 