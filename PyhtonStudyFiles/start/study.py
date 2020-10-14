# 字符和字符串
# in and not in
# 运算符：+、-、*、/、**、//、=、==、!=
# 布尔值 Ture False
# and or 的计算 :从前往后
# 赋值运算：+=、-=、*=、/=、%=

# 基本数据类型：数字int，字符串str，布尔值，列表list，元组tuple，字典dict
# 数字：int long
# python3里面都是int
# 数字常用：.int 将字符串转换为数字
# a=“123”
# b=int(a)
# 按着某种进制转换 b=int(num,base=进制选择)
# age.bit_length()   最少使用二进制的位数
# 字符串：.capitalize() 首字母大写
#         .casefold() 所有变小写，很多未知也可小写
#         .lower()字母小写
#         .silower()
#         .upper()
#         .isupper
#         .center(9,"中") 设置宽度将内容居中，两边宽度可填冲单个字符
#         .ljust()      .rjust()   右边填充和左边填充  和center相似
#         .count('e',5.6) 找字符串中子序列出现的次数，可以设置起始和结束的位置
#         .encode()
#         .decode()
#         .endswith('') 以什么结尾  .startwith('') 以什么开始
#         .find(‘’，5，8) 从开始往后找，找到第一个获取其位置，可以设置查找区间，左闭右开,未找到返回-1
#         .format()格式化 将字符串中的一个占位符替换 有两种方式，指定和数字顺序
#         .format_map()
#            .index 和find功能相同找不到返回报错 不用
#         .isalnum() 判断内部是否只有字母字符串
#         .isalpha()判断是否是字母和汉字
#         .isdecimal()    .isdigit()   .isnumeric()判断是否是数字，包括特殊数字，包括中文数字
#         .expandtabs()断句，是否有\t，有的话进行补充空格   可以用于制表
#         .isidentifer()判断是否是标识符，由字母下划线数字组成，数字不做开头
#         .isprintable()内部是否有打印不显示的例如\t,\n
#         .isspace()是否全部是空格
#         .istitle()判断是否英文字符串内部单词首字母都是大写，即标题
#         .title()转换为标题
# *****   .join()某一个字符加入到某一字符串中的字符间
#         .lstrip()从左边开始寻找删除内容，包括空白,\t,\n,可加参数制定删除子序列，没有时停止
#         .rstrip()从左边开始寻找删除内容，包括空格,\t,\n,可加参数制定删除子序列，没有时停止
#         .strip()寻找删除内容，包括右边空格,\t,\n,可加参数制定删除子序列，没有停止
#         .partition()根据某项分割，保留某项，只能分割一次
#         .rpartition()
#         .split()根据某项分割，无法保留某项，分割次数任意
#         .rsplit()
# 正则表达式，两种分割的集合
#         .swapcase()大小写转换

# def xiadan():
#     ret=[]
#     for i in  range(100):
#         ret.append('egg%s' %i)
#         return ret
# print(xiadan())

# def xiadan():
#     for i in  range(100):
#         yield 'egg%s' %i
#
# jidan=xiadan()
#
# x=jidan.__next__()
# print(x)
# x=jidan.__next__()
# print(x)
# x=jidan.__next__()
# print(x)
#
# s=('a%s' %i for i in range(10))
# print(s)

# def fa():
#     name='woziji'
#     def dad():
#         # name='bieren'
#         print('%s' %locals())
#     dad()
# fa()


