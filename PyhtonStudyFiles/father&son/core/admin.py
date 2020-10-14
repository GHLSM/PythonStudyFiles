from interface import admin_interface
from interface import commen_interface
from lib import commen


admin_info = {
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
            flag, msg = admin_interface.admin_register(
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
        flag, msg = commen_interface.login_interface(username, password, usertype = 'admin')
        if flag:
            print(msg)
            admin_info['username'] = username
            break
        else:
            print(msg)


@commen.auth_func('admin')
def create_school():
    while True:
        school_name = input('请输入学校名称：').strip()
        school_addr = input('请输入学校地址：').strip()
        flag, msg = admin_interface.create_school_interface(
            school_name, school_addr, admin_info.get('username')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


@commen.auth_func('admin')
def create_lesson():
    # 管理员先选择学校，输入课程名称，调用接口创建课程
    while True:
        flag, school_list_or_msg = commen_interface.get_all_school_interface()
        if flag:
            print(school_list_or_msg)
            # break
        for index, school_name in enumerate(school_list_or_msg):
            print('学校编号为：%s，学校名称为：%s' % (index, school_name))

        choice = input('请输入学校编号：').strip()

        if not choice.isdigit():
            print('请输入正确编号：')
            continue
        else:
            choice = int(choice)
        if choice not in range(len(school_list_or_msg)):
            print('请输入正确编号：')
            continue

        school_name = school_list_or_msg[choice]
        lesson_name = input('请输入需要创建的课程名称：').strip()
        lesson_time = input('请输入课程时长：').strip()
        lesson_much = input('请输入课程价格：').strip()

        flag, msg = admin_interface.create_lesson_interface(
            school_name, lesson_name, lesson_time, lesson_much, admin_info.get('username')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


@commen.auth_func('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师的名字：').strip()
        teacher_school = input('请输入老师所属校区：').strip()
        flag, msg = admin_interface.create_teacher_interface(
            teacher_name, teacher_school, admin_info.get('username')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_lesson,
    '5': create_teacher,
}


def admin_view():
    while True:
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建课程（先选择学校）
        5.创建讲师
        (输入 q 退出对话)
        ''')
        choice = input('请输入功能编号:').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('您的输入有误，重新输入！')
            continue

        func_dic.get(choice)()
