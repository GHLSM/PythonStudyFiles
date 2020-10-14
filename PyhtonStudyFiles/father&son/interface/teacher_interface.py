from db import models
from interface import commen_interface


def check_lesson_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if not teacher_obj.lesson_list_teacher:
        return False, '您未选择课程'
    else:
        return True, teacher_obj.lesson_list_teacher


def choose_lesson_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    school_obj = models.School.select(teacher_obj.con_school)
    if not school_obj.lesson_list:
        return False,'您选择的学校还未开设课程'
    print('以下为学校开设课程\n')
    for index ,lesson_name in enumerate(school_obj.lesson_list):
        print('课程编号为：%s，课程名称为%s' %(index, lesson_name))

    choice = input('请输入您想选择的课程编号：').strip()
    if not choice:
        return False, '您的输入为空！'
    if choice.isdigit():
        choice = int(choice)
    else:
        return False, '请输入数字编号!'

    if choice in range(len(school_obj.lesson_list)):
        teacher_obj.lesson_list_teacher.append(school_obj.lesson_list[choice])
        teacher_obj.save()
        return True, '您已选择教授课程%s' % school_obj.lesson_list[choice]
    else:
        return False, '您的输入有误，请重新输入！'

def check_stu_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if not teacher_obj.lesson_list_teacher:
        return False, '您还没有选择课程'

    for index, lesson_name in enumerate(teacher_obj.lesson_list_teacher):
        print('您已选择以下教学课程：\n课程编号为%s，课程名称为%s' % (index, lesson_name))
        choice = input('请输入您想查看学生的课程编号：').strip()
        if not choice:
            return False, '您的输入为空！'
        if choice.isdigit():
            choice = int(choice)
        else:
            return False, '请输入数字编号!'

        if choice in range(len(teacher_obj.lesson_list_teacher)):
            lesson_obj = models.Lesson.select(teacher_obj.lesson_list_teacher[choice])
            print( '您已选择教授课程%s' % teacher_obj.lesson_list_teacher[choice])
            return True, lesson_obj.student_list
        else:
            return False, '您的输入有误，请重新输入！'












