def school(name, addr, type):
    def int_t(name, addr, type):
        school_thing = {
            'name': name,
            'addr': addr,
            'type': type,
            'exam': exam,
            'enrollment':enrollment,
        }
        return school_thing
    def exam(school):
        print('school %s now in exam' %name)
    def enrollment(school):
        print('now in enrollment')
    return int_t(name, addr, type)
s1=school('tianzhong' ,'tianchang','gongli')

