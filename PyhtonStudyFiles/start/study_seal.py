class People:
    __star='earth' #_peopele__earth='earth'
    def __init__(self,ID_num,name,age):
        self.ID_num=ID_num
        self.name=name
        self.age=age
    def get_ID(self):
        print('我是内部方法，我可以得到ID是【%s】' %self.ID_num)
    def get_star(self): ##访问函数（接口）
        print(self.__star)
# # print(People.__earth)
# # print(People._People__star)
Per1=People('341181','gh','23')
Per1.get_star() #实现访问操作
                #有点类似给类打孔