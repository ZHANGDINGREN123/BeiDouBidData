import numpy as np
import re
import jieba
import jieba.analyse
import cx_Oracle
import os
import sys

def Security_Word_Cloud(dateBegin,dateEnd):
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
    sql = "SELECT * FROM (SELECT S_PROBLEMDESCRIPTION AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "GROUP BY S_PROBLEMDESCRIPTION) t ORDER BY t.count DESC"
    sqltest = "SELECT * FROM (SELECT S_PROBLEMDESCRIPTION AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-08-23' GROUP BY S_PROBLEMDESCRIPTION) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        c.execute(sql_2)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    lines = a
    clean_lines = []
    for sentence in lines:
        if sentence is np.nan:
            continue
        clean_lines.append(re.sub('\d*','',str(sentence)))
    Key_word = []
    for sentence in clean_lines:
        Key_word.append(jieba.analyse.extract_tags(sentence, topK=5, withWeight=False,allowPOS=()))
    Key = [item for sub_list in Key_word for item in sub_list]
    d = {x: Key.count(x) for x in Key}
    # for i in range(50):
    #     # sorted(d, key=lambda x: d[x])[-(i+1)]
    #     print(sorted(d, key=lambda x: d[x])[-(i+1)])
    d3 = {k: v for k, v in d.items() if v > 15}
    # print(d3)
    c.close()
    conn.close()
    return d3
e = Security_Word_Cloud('2017-07-22','2017-08-22')
# print(e)
