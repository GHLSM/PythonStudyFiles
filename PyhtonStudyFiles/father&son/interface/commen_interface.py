import os
from conf import settings
from db import models

def get_all_school_interface():
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )
    if not os.path.exists(school_dir):
        return False, '没有学校，请先联系管理员'
    school_list = os.listdir(school_dir)

    return True, school_list
#
def login_interface(username, password, usertype):
    obj = None
    if usertype == 'admin':
        obj = models.Admin.select(username)
    if usertype == 'student':
        obj = models.Student.select(username)
    if usertype == 'teacher':
        obj = models.Teacher.select(username)
    if obj:
        if password == obj.password:
            return True, '登陆成功！'
        else:
            return False, '您输入的密码有误！'
    else:
        return False, '用户不存在！'

def last_level_back():
    pass

# def get_all_school_addr_interface():
#     school_dir = os.path.join(
#         settings.DB_PATH, 'School'
#     )
#     if not os.path.exists(school_dir):
#         return False, '没有学校，请先联系管理员'
#     school_list = os.listdir(school_dir)
#     school_addr_list = []
#     for school_name in school_list:
#         school_obj = models.School.select(school_name)
#         school_addr_list.append(school_obj.addr)
#     return True, school_addr_list
#



