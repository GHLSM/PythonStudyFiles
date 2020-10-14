from db import models
from interface import commen_interface

def admin_register(username, password):
    # 判断用户是否存在
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, '用户已存在！'
    # 存在不允许注册，返回用户已存在
    # 不存在，调用类实例化得到对象保存
    admin_obj = models.Admin(username, password)
    admin_obj.save()
    return True, '注册成功！'


# def admin_login_interface(username, password):
#     flag, msg= commen_interface.login_interface(username, password, usertype = 'admin')
#     return flag, msg


def create_school_interface(school_name, school_addr, admin_name):
    # 查看学校是否存在
    school_obj = models.School.select(school_name)
    # 存在不允许注册，返回学校已存在
    if school_obj:
        return False, '学校已存在！'
    # 不存在，调用类实例化得到对象保存
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(
        school_name, school_addr
    )
    return True, '学校%s创建成功！' % school_name


def create_lesson_interface(school_name, lesson_name, lesson_time, lesson_much, admin_name):
    # 查看课程是否存在，先获取学校对象的课程列表，判断当前课程是否存在课程列表中
    school_obj = models.School.select(school_name)
    if lesson_name in school_obj.lesson_list:
        return False, '当前课程已存在！'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_lesson(
        school_obj, lesson_name, lesson_time, lesson_much
    )
    return True, '%s 课程创建成功，绑定校区为%s' % (lesson_name, school_name)


def create_teacher_interface(teacher_name, teacher_school, admin_name):
    teacher_obj = models.Teacher.select(teacher_name)
    school_obj = models.School.select(teacher_school)
    if not school_obj:
        return False,'学校不存在'
    if teacher_obj:
        return False, '老师%s已存在' %teacher_name
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_school)
    return True, '%s老师创建成功！' %teacher_name







