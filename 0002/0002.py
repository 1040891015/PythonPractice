# -*- coding:utf-8 -*-

import os.path
import sys
import pymysql


def execute_sql(sql):
    db = pymysql.connect('localhost', 'root', 'jin123456', 'test') # 打开数据库连接
    cursor = db.cursor() # 使用cursor()方法创建一个游标对象
    try:
        cursor.execute(sql) # 使用execute()方法执行SQL语句
        db.commit() # 提交执行
    except:
        db.rollback() # 如果发生错误则回滚
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接

if __name__ == '__main__':
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    keyfile = os.path.dirname(dirname) + os.sep + '0001' + os.sep + 'outfile.txt'
    execute_sql('drop table if exists testkey;')
    sql = '''create table TESTKEY (
            KEYVALUE CHAR(20) NOT NULL,
            UPDATETIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)'''
    execute_sql(sql)
    with open(keyfile,'r') as f:
        for line in f:
            if line:
                sql = '''insert into testkey(KEYVALUE) values('%s');''' % line[0:-1]
                execute_sql(sql)
    