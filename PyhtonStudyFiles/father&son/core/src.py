from core import admin, student, teacher

view_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


def run():
    while True:
        print('''
        ========欢迎来到选课系统=======
                 1、管理员功能
                 2、学生功能
                 3、老师功能
        ===============end=============''')

        choice = input('请输入功能编号:').strip()
        if choice not in view_dic:
            print('您的输入有误，重新输入！')
            continue
        view_dic.get(choice)()
