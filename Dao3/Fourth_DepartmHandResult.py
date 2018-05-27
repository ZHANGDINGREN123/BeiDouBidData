# -*- coding: UTF-8 -*-

import cx_Oracle
import os
import sys
from OracleConnect import oracle_connect


def Fourth_Layer_Two(dateBegin, dateEnd, Check_Department=None, Pull_HandResult=None, People_Depart=None):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
        Check_Department = "站领导"
        Pull_HandResult = "红通"
        People_Depart = "任智斌"

    conn = oracle_connect.ora_con()
    # try:
    #     conn = cx_Oracle.connect("MASTER/123456@172.21.176.157/XE")
    # except Exception:
    #     print("数据库连接出错",Exception)
    #     conn.close()
    #     sys.exit(1)

    sql = r"SELECT * FROM (SELECT S_CHECKDEPARTMENT,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    if Check_Department != None:
        sql = r"SELECT * FROM (SELECT S_HANDLEREASULT,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    if Pull_HandResult != None:
        sql = r"SELECT * FROM (SELECT S_CHECKPERSON,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    if People_Depart != None:
        sql = r"SELECT * FROM (SELECT S_CHECKWAY,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd+ "'"
    sql_final = sql_2 + " GROUP BY S_CHECKDEPARTMENT) t ORDER BY t.count DESC "
    if Check_Department != None:
        sql_3 = sql_2 + " AND S_CHECKDEPARTMENT = '"+Check_Department + "'"
        sql_final = sql_3 + " GROUP BY S_HANDLEREASULT) t ORDER BY t.count DESC "
    if Pull_HandResult != None:
        sql_4 = sql_3 + " AND S_HANDLEREASULT = '" + Pull_HandResult + "'"
        sql_final = sql_4 + " GROUP BY S_CHECKPERSON) t ORDER BY t.count DESC "
    if People_Depart != None:
        sql_5 = sql_4 + " AND S_CHECKPERSON = '" + People_Depart + "'"
        sql_final = sql_5 + " GROUP BY S_CHECKWAY) t ORDER BY t.count DESC "
    # sql_final +=  " GROUP BY S_CHECKWAY) t ORDER BY t.count DESC "
    # sqltest = "SELECT * FROM (SELECT S_CHECKPERSON,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-08-23' AND S_CHECKDEPARTMENT = '站领导' AND S_HANDLEREASULT = '红通' AND S_EMPLOYEECODE = '100008' GROUP BY S_CHECKPERSON) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        print(sql_final)
        c.execute(sql_final)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    dic_a = dict(a)

    c.close()
    conn.close()
    if People_Depart != None:
        return dic_a, People_Depart
    if Pull_HandResult != None:
        return dic_a, Pull_HandResult
    if Check_Department != None:
        return dic_a, Check_Department

    return dic_a,None

if __name__ == "__main__":
    print(type(Fourth_Layer_Two(None,None,"站领导", "红通")))