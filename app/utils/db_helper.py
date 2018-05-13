import pymysql
from DBUtils.PooledDB import PooledDB

pool = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=2,
    blocking=True,
    maxusage=None,
    ping=4,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='pss123546',
    database='pooldb',
    charset='utf8'

)


class SQLHelper(object):

    @staticmethod
    def fetch_one(sql, args):
        conn = pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fethone()

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def fetch_all(sql, args):
        conn = pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fethall()
        cursor.close()
        conn.close()
        return result
