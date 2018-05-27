import numpy as np
import re
import jieba
import jieba.analyse
import cx_Oracle
import os
import sys

def new_fault_show(dateBegin,dateEnd):
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
    sql = "SELECT * FROM (SELECT S_FAULTPOSITION,COUNT(1) AS count FROM EQ_FAULT WHERE to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "GROUP BY S_FAULTPOSITION) t ORDER BY t.count DESC"
    sqltest = "SELECT * FROM (SELECT S_FAULTPOSITION ,COUNT(1) AS count FROM EQ_FAULT WHERE to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')<='2017-08-23' GROUP BY S_FAULTPOSITION) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        c.execute(sql_2)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    dic_a = dict(a)
    # print(dic_a)
    c.close()
    conn.close()
    return dic_a

#
# e = new_fault_show('2017-01-22','2017-08-22')
# print(e)
