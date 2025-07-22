from DbManager import DbManager
from Student import Student
import datetime

class App():
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Student List\n2-Add Student\n3-Edit Student\n4-Delete Student\n5-Close(E/C)"

        while True:
            print(msg)
            choose = input("Your Choises: ")

            if choose == "1":
                self.displayStudents()
            elif choose == "2":
                self.addStudent()
            elif choose == "3":
                self.editStudent()
            elif choose == "4":
                self.deleteStudent()
            elif (choose == "E" or choose == "e") or (choose == "C" or choose == "c"):
                print("Closed.")
                break

    def deleteStudent(self):
        classId = self.displayStudents()
        studentId = int(input("Student Id: "))

        self.db.deleteStudent(studentId)

    def displayclasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.Id}:{c.name}")

    def editStudent(self):
        classId = self.displayStudents()
        studentid = int(input("Student Id: "))

        student = self.db.GetStudentById(studentid)

        student[0].studentname = input("Name: ") or student[0].studentname
        student[0].studentsurname = input("SurName: ") or student[0].studentsurname
        student[0].studentgender = input("Gender (E/K): ") or student[0].studentgender
        student[0].studentnumber = int(input("Number: ")) or student[0].studentnumber
        student[0].classId = input("Class: ") or student[0].student.classId

        year = int(input("Birthday Year: "))
        month = int(input("Birthday Month(Number): "))
        day = int(input("Birthday Day: "))

        student[0].studentbirthday = datetime.date(year,month,day)
        self.db.EditStudent(student[0])


    def addStudent(self):
        self.displayclasses()

        classid = int(input("Which Class Do You Want To Add?: "))
        number = input("What Is Student Number?: ")
        name = input("Student Name?: ")
        surname = input("Student SurName?: ")
        gender = input("Student Gender? (G/B): ")
        year = int(input("Student Birthday Year?: "))
        month = int(input("Student Birthday Month? (Number): "))
        day = int(input("Student Birthday Day?: "))
        birthdate = datetime.date(year,month,day)

        student = Student(None,number,name,surname,gender,birthdate,classid)
        self.db.AddStudent(student)

    def displayStudents(self): 
        self.displayclasses()      
        classId = int(input("which Class (Write ClassId): "))

        student = self.db.GetStudentsByClassId(classId)
        print("Student List:")
        for std in student:
            print(f"{std.Id}-{std.studentname} {std.studentsurname}")
        return classId
    

db = App()
db.initApp()