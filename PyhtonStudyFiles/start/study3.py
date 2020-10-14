# import json
#
# a = '{"name":"alex"}'
# b='8'
# c='[11,22]'
# with open('hello', 'w') as f:
#     f.write(b + '\n')
#     f.write(a + '\n')
#
#     f.write(c)
#
# with open('hello', 'r') as f:
#     # data = json.loads(f.readline())
#     data = f.readlines()
# print(data)
#
# import logging
#
#
# logging.basicConfig(
#     level=logging.INFO,
#     filename='logger',
#     filemode='w',
#     format='%(asctime)s %(message)s'
#  )
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')



# import logging
#
# def logger():
#     logger=logging.getLogger()
#     logger.setLevel('INFO')
#     fh = logging.FileHandler('log_new')
#     sh = logging.StreamHandler()
#     fm = logging.Formatter('%(asctime)s------%(message)s')
#     fh.setFormatter(fm)
#     sh.setFormatter(fm)
#     logger.addHandler(fh)
#     logger.addHandler(sh)
#     return logger
#
# logger()
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


