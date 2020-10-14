from db import db_handle
'''专门用于管理所有的类'''
'''
学校，学员，课程，讲师，管理员
'''



class Base:
    def save(self):
        db_handle.save_data(self)

    @classmethod
    def select(cls, username):
        obj = db_handle.select_data(cls, username)
        return obj


class Admin(Base):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_teacher(self,teacher_name, teacher_school, teacher_pwd = '123'):
        teacher_obj = Teacher(teacher_name, teacher_school, teacher_pwd)
        teacher_obj.save()

    def create_lesson(self, school_obj, lesson_name, lesson_time, lesson_much):
        # 调用课程类。创建课程对象，获取学校对象，添加到学校课程列表中
        lesson_obj = Lesson(lesson_name, lesson_time, lesson_much)
        lesson_obj.save()
        school_obj.lesson_list.append(lesson_name)
        school_obj.save()



class School(Base):
    def __init__(self, name, addr):
        self.username = name
        self.addr = addr
        self.lesson_list = []
        self.have_student_list = []


class Student(Base):
    def __init__(self, username, password, school_name = None):
        self.username = username
        self.password = password
        self.have_lesson_list = []
        self.score_list = []
        self.con_school = school_name
        self.lesson_score = None


class Lesson(Base):
    def __init__(self, lesson_name, lesson_time, lesson_much):
        self.username = lesson_name
        self.time = lesson_time
        self.money = lesson_much
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, teacher_school, teacher_pwd):
        self.username = teacher_name
        self.password = teacher_pwd
        self.con_school = teacher_school
        self.lesson_list_teacher = []