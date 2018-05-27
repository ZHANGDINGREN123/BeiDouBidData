import cx_Oracle
import os
import sys


def ora_con():
    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.157/XE")
    except Exception:
        print("数据库连接出错", Exception)
        conn.close()
        sys.exit(1)
    return conn