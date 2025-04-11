class Student:
    def __init__(self,student_id,name,department,is_enrolled=False):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=is_enrolled
        
    def enroll_student(self):
        if self.__is_enrolled:
            print('Already Enrolled') 
        else:
            self.__is_enrolled=True
            StudentDatabase.add_student(self)
            print(f'Enrolled {self.__name}')
            
    def drop_student(self):
        if self.__is_enrolled==False:
            print('Not a student')
        else:
            self.__is_enrolled=False
            print(f'Droped {self.__name}')
    def view_student_info(self):
        print(f'ID: {self.__student_id} NAME: {self.__name} DEPT: {self.__department} ENROLLED: {self.__is_enrolled}')
    
    def get_id(self):
        return self.__student_id

class StudentDatabase:
    student_list=[]
    @classmethod
    def add_student(self,student):
        self.student_list.append(student)
    @classmethod
    def get_students(self):
        return self.student_list

while True:
    print("""1. View All Students
2. Enroll Student
3. Drop Student
4. Exit
 """)
    cmd=input('Enter a number: ')

    if cmd=='1':
        students=StudentDatabase.get_students()
        print('---------------Our Student--------------')
        for student in students:
            student.view_student_info()
    elif cmd=='2':
        id=input('Enter ID(Any positive Integer(1'
        '-999)):')
        if not id.isdigit():
            print('Invalid')
            continue
        id2=int(id)
        if id2<=0 or id2>999:
            print('Invalid')
            continue
        name=input('Enter Name:')
        dept=input('Enter Department:')
        student=Student(id,name,dept)
        student.enroll_student()
    elif cmd=='3':
        id=input('Enter ID(Any positive Integer(1-999)):')
        if not id.isdigit():
            print('Invalid')
            continue
        id2=int(id)
        if id2<=0 or id2>999:
            print('Invalid')
            continue
        flag=False
        for student in students:
            if student.get_id()==id:
                student.drop_student()
                flag=True
                break
        if flag==False:
            print('Not a Student')
    elif cmd=='4':
        print("Exit!")
        break
    else:
        print('Invalid choice!')

