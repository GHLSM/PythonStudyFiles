#反射：指程序可以访问，检测，修改它本身各种属性的能力
class BlackMedium:
    feture = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print('[%s]正在卖房子' %self.name)

    def ret_house(self):
        print('[%s]正在租房子' %self.name)

# b1=BlackMedium('万城置地', '天路元')
# print(hasattr(b1,'name'),hasattr(b1,'sell_house')) #hasatter方法,Ture or False
# print(getattr(b1,'sell_house')) #getattr,没有报错
# print(getattr(b1,'sell_house','没有这个属性')) #找不到不报错，输出3号位内容
# setattr(b1,'新数据属性','新数据属性的value') #b1.***=*** ,可以用于修改属性
# delattr(b1,'删除的数据属性') #删除属性  ==del bi.***

import sys
f1=sys.modules[__name__]
print('==>',hasattr(f1,'BlackMedium'))