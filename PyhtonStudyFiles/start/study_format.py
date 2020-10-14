# class Date:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#
#     def __format__(self, format_spec):
#         print('run')
#         return 'x'
#
# D1=Date(2016, 12, 26)
# print('{0.year}:{0.month}:{0.day}'.format(D1))##2016:12:26
# print('{0}:{0}:{0}'.format(D1))
# ###   2016:12:26
# ###   run
# ###   run
# ###   run
# ###   x:x:x