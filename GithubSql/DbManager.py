import mysql.connector
from datetime import datetime
from Connection import connection
from Student import Student
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Error...",err)

    def deleteStudent(self,studentId):
        sql = "DELETE from student where Id = %s"
        value = (studentId,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} - records were deleted.")
        except mysql.connector.Error as err:
            print("Error..",err)

    def GetStudentById(self,id):
        sql = "SELECT * FROM student where id = %s"
        values = (id,)
        self.cursor.execute(sql,values)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error..",err)

    def GetStudentsByClassId(self,ClassId):
        sql = "SELECT * FROM student where ClassId = %s"
        values = (ClassId,)
        self.cursor.execute(sql,values)
        try:
           obj = self.cursor.fetchall()
           return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
           print("Error..",err)

    def AddStudent(self,student: Student):
        sql = "INSERT INTO Student(StudentNumber,StudentName,StudentSurname,StudentGender,StudentBirthday,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentnumber,student.studentname,student.studentsurname,student.studentgender,student.studentbirthday,student.classid)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} records were added.")
        except mysql.connector.Error as err:
            print("Error..",err)
    
    def EditStudent(self,student : Student):
        sql = "UPDATE Student set StudentNumber=%s,studentname=%s,studentsurname=%s,studentgender=%s,studentbirthday=%s,classid=%s where id = %s"
        values = (student.studentnumber,student.studentname,student.studentsurname,student.studentgender,student.studentbirthday,student.classid,student.Id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} records were updated.")
        except mysql.connector.Error as err:
            print("Error..",err)

db = DbManager()
