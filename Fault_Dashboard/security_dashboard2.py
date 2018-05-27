# -*- coding: UTF-8 -*-

import cx_Oracle
import os
import sys



# 给定参数获取结果，等待前端Request（get/post）传递参数，py调用该方法再response结果
# TODO:时间应该所有方法共用
def show_security_dashboard2(dateBegin, dateEnd):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.157/XE")
    except Exception:
        print("数据库连接出错",Exception)
        conn.close()
        sys.exit(1)

    sql1 = "SELECT  max(S_RESPONSIBLEPERSON) FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql1_1 = sql1 + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql1_2 = sql1_1 + dateEnd + "'" + ""
    sql1_test = "SELECT max(S_RESPONSIBLEPERSON) FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-06-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-07-13'"
    c4 = conn.cursor()
    try:
        c4.execute(sql1_2)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c4.close()
        conn.close()
        sys.exit(1)
    a = c4.fetchall()
    c4.close()
    conn.close()
    return a

# e = show_security_dashboard2('2017-07-20', '2017-07-22')
# print(e)

