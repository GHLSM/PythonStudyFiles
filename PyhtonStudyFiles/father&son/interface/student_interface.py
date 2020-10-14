from db import models
from interface import commen_interface

def student_register(username, password):
    student_obj = models.Student.select(username)
    if  student_obj:
        return False,'学生%s已存在' %username

    student_obj = models.Student(username, password)
    student_obj.save()
    return True, '学生%s注册成功' %username

#
# def student_login_interface(username, password):
#     flag, msg= commen_interface.login_interface(username, password, usertype = 'student')
#     return flag, msg


def choose_school_interface(student_name):
    flag, school_list_or_msg = commen_interface.get_all_school_interface()
    if flag:
        print('以下是目前的学校信息：\n')

        for index, school_name in enumerate(school_list_or_msg):
            print('学校：%s，编号为：%s' % (school_name, index))

        choice = input('请输入您选择的学校编号').strip()

        if not choice:
            return False, '您的输入为空，请重新选择'

        if choice.isdigit():
            choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            return '请输入正确的编号!'

        chosen_school = school_list_or_msg[choice]
    else:
        return False, '没有学校，请先联系管理员'

    student_obj = models.Student.select(student_name)
    # student_obj.con_school.append(chosen_school)
    # student_obj.save()
    if not student_obj.con_school:
        student_obj.con_school = chosen_school
        student_obj.save()
        school_obj = models.School.select(chosen_school)
        school_obj.have_student_list.append(student_name)
        school_obj.save()
        return True, '学生%s已选择学校%s' %(student_name,chosen_school)
    else:
        return False, '您已经选择过学校了'


def choose_lesson_interface(student_name):
    student_obj = models.Student.select(student_name)
    school_name = student_obj.con_school
    school_obj = models.School.select(school_name)

    if not school_obj.lesson_list:
        return False, '学校暂未开设课程，请联系管理员'

    for index, lesson_name in enumerate(school_obj.lesson_list):
        lesson_obj = models.Lesson.select(lesson_name)
        print('学校开设了课程%s，课程编号为%s\n此课程周期为%s，学费为%s\n\n' % (lesson_obj.username, index, lesson_obj.time, lesson_obj.money))

    choice = input('请输入你想选择的课程编号').strip()
    if not choice:
        return False, '您的输入有误，选课失败!'

    if choice.isdigit():
        choice = int(choice)
    else:
        return False, '请输入数字编号!'

    if choice in range(len(school_obj.lesson_list)):
        if school_obj.lesson_list[choice] in student_obj.have_lesson_list:
            return False, '您已选择这门课，不可重复选择'
        else:
            student_obj.have_lesson_list.append(school_obj.lesson_list[choice])
            student_obj.save()
            return True, '选择课程%s 成功' % school_obj.lesson_list[choice]
    else:
        return False, '您的输入有误，选课失败!'

def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    for index, lesson_name in enumerate(student_obj.have_lesson_list):
        print('你已经选择的课程有\n课程编号为%s，课程名称为%s' % (index, lesson_name))

    check_lesson_index = input('请输入你想查看的课程代号：').strip()
    if not check_lesson_index:
        return False, '输入为空！'
    if check_lesson_index.isdigit():
        check_lesson_index = int(check_lesson_index)
    else:
        return False, '请输入数字编号！'

    if check_lesson_index in range(len(student_obj.have_lesson_list)):
        check_lesson = student_obj.have_lesson_list[check_lesson_index]
        if check_lesson_index not in range(len(student_obj.score_list)):
            return False, '您的课程还未登分'
        else:
            score = student_obj.score_list[check_lesson_index]
            return True, '课程%s的分数为%s' % (check_lesson, score)
    else:
        return False, '您的输入有误，请输入正确的课程编号'
