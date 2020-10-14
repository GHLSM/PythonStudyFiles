# import time
#
#
# def func1():
#     while True:
#         res = 1000000 + 1
#         yield
#
# def func2():
#     g = func1()
#     for i in range(1000000):
#         os = i + 1
#         next(g)
#
# start_time = time.time()
# func2()
# print(time.time() - start_time)


