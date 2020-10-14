# class Foo:
#     def __init__(self,x):
#         self.x=x
#
#     def __getattr__(self, item):
#         print("run getattr")
#
#     def __getattribute__(self, item):  #无论属性能否找到都先触发
#         print('run getattribute')       #当getattribute抛出异常的时候才会触发getattr
#         raise AttributeError('error')
#
# f1=Foo(10)
# # print(isinstance(f1,Foo))  #是否是实例
# #                             #True
# # class Bar(Foo):
# #     pass
# #
# # print(issubclass(Bar,Foo)) #是否是子级
# #                             #Ture
# f1.x
# f1.xxxxxxxx

# class Foo:
#     def __getitem__(self, item):
#         print('getitem')
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         print('setitem')
#         self.__dict__[key]=value
#
#     def __delitem__(self, key):
#         print('delitem')
#         self.__dict__.pop(key)
# f1=Foo()
# f1['name']='alex'
# f1['age']=22
# print(f1.__dict__)##字典形式访问item方法
# del f1.name      ##用点的形式访问attr方法
# print(f1.__dict__)
# del f1['name']
# print(f1.__dict__)

class Foo:
    # def __str__(self):    ##用于print中
    #     return '自己定制的名称'
    def __repr__(self):    ##在解释器中用，直接F1得到返回值
        return '定制的名称'

    def __init__(self,name,age):
        self.name=name
        self.sge=age

F1=Foo('alex', 18)
print(F1)   ##str(F1)--->F1.__str__()----->F1.__repr__()


