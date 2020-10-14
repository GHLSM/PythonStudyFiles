from lib import commen
from interface import student_interface
from interface import commen_interface

student_info = {
    'username': None
}


def register():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请重新输入密码').strip()

        if not password:
            print('您的密码为空，请重新输入！')
            continue
        if password == re_password:
            flag, msg = student_interface.student_register(
                username, password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('您输入的密码不一致，请重新输入！')


def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag, msg =  commen_interface.login_interface(username, password, usertype = 'student')
        if flag:
            print(msg)
            student_info['username'] = username
            break
        else:
            print(msg)
            break


@commen.auth_func('student')
def choose_school():
    # 先获取所有校区信息，打印所有的学校
    while True:
        # flag, school_list_or_msg = commen_interface.get_all_school_interface()
        # if flag:
        #     print('以下是目前的学校信息：\n')
        #
        #     for index, school_name in enumerate(school_list_or_msg):
        #         print('学校：%s，编号为：%s' % (school_name, index))
        #
        #     choice = input('请输入您选择的学校编号').strip()
        #     if not choice:
        #         print('您的输入为空，请重新选择')
        #         continue
        #
        #     if choice.isdigit():
        #         choice = int(choice)
        #
        #     if choice not in range(len(school_list_or_msg)):
        #         print('请输入正确的编号!')
        #         continue
        #
        #     chosen_school = school_list_or_msg[choice]

            flag, msg = student_interface.choose_school_interface(
                student_info.get('username')
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)


@commen.auth_func('student')
def choose_lesson():
    # 获得已经选择的学校，选择学校
    # 获得每个学校开设的课程，选择，绑定
    while True:
        flag, msg = student_interface.choose_lesson_interface(
            student_info.get('username')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


@commen.auth_func('student')
def check_score():
    while True:
        flag, msg = student_interface.check_score_interface(
            student_info.get('username')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_lesson,
    '5': check_score,
}


def student_view():
    while True:
        print('''
        1.注册
        2.登录
        3.选择校区
        4.选择课程
        5.查看分数
        (输入 q 退出对话)
        ''')
        choice = input('请输入功能编号').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('您的输入有误，重新输入！')
            continue

        func_dic.get(choice)()
