from lib import commen
from interface import commen_interface
from interface import teacher_interface


teacher_info = {
    'username':None
}

def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag, msg = commen_interface.login_interface(username, password, usertype='teacher')
        if flag:
            print(msg)
            teacher_info['username'] = username
            break
        else:
            print(msg)


@commen.auth_func('teacher')
def check_lesson():
    while True:
        flag, msg = teacher_interface.check_lesson_interface(
            teacher_info.get('username')
        )
        if flag:
            print('您可以选择的课程有：')
            for i in msg:
                print(i)
            break
        else:
            print(msg)
            break



@commen.auth_func('teacher')
def choose_lesson_teacher():
    while True:
        flag, msg = teacher_interface.choose_lesson_interface(
            teacher_info.get('username')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break



@commen.auth_func('teacher')
def check_stu():
    while True:
        flag, msg = teacher_interface.check_stu_interface(
            teacher_info.get('username')
        )
        if flag:
            print('学生列表为：',msg)
            break
        else:
            print(msg)
            break

@commen.auth_func('teacher')
def change_score():
    pass




func_dic = {
    '1': login,
    '2': check_lesson,
    '3': choose_lesson_teacher,
    '4': check_stu,
    '5': change_score,
}

def teacher_view():
    while True:
        print('''
        1.登录
        2.查看教授课程
        3.选择教授课程
        4.查看课程下学生
        5.修改学生分数
        (输入 q 退出对话)
        ''')
        choice = input('请输入功能编号').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('您的输入有误，重新输入！')
            continue


        func_dic.get(choice)()