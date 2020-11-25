import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'ghalsm',
    database = 'study',
    charset = 'utf8',
    autocommit = True
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'insert into dep(dep_name, dep_desc) values (%s,%s)'
# affect_rows_num = cursor.execute(sql,('win','good'))
affect_rows_num = cursor.executemany(sql,[('win','good'),('unix','maybe')])
print(affect_rows_num)
# conn.commit()
