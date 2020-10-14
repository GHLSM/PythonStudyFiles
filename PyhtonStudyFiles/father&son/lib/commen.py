
def auth_func(role):  # 多用户登录认证装饰器
    from core import admin, student, teacher

    def login_auth(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['username']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif role == 'student':
                if student.student_info['username']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if teacher.teacher_info['username']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print('您没有权限')
        return inner
    return login_auth
