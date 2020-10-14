class Foo:
    x=1
    def __init__(self,y):
        self.y=y
    def __getattr__(self, item):
        print('run __getattr__')
    def __delattr__(self, item):
        print('run __delattr__')
    def __setattr__(self, key, value):
        print('run __setattr__')
        # self.key=value #会进入死循环，因为只要进行设置属性就会触发__setattr__
        self.__dict__[key]=value
# f1=Foo(10)
# print(f1.y)
# print(getattr(f1,'y'))
# f1.aaaaa #字符串不存在时，__getattr__会运行#run __getattr__
# del f1.y #删除的时候会运行__delattr__
# f1.z=3
# print(f1.__dict__)
