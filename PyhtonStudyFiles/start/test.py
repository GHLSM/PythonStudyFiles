import pymysql

class Mine_pysql():
    def __enter__(self):
        print("我在with管理时，会触发，返回值赋给as后面的变量")
        self.conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="ghalsm",database="db01")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出代码块时，执行此方法")
        self.conn.close()
        print("1: %s", exc_type)
        print("1: %s", exc_val)
        print("1: %s", exc_tb)

with Mine_pysql() as conn:
    # 操作语句,先获取游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


