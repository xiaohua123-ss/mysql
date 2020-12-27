import traceback, dbutils.pooled_db

import pymysql

SQL = "INSERT INTO user(name,note) VALUES('小李老师', 'aaa')"


def main():
    try:
        pool = dbutils.pooled_db.PooledDB(creator=pymysql, mincached=2, maxcached=5, maxconnections=20, blocking=True,
                                          host='localhost',
                                          port=3306,
                                          user='root',
                                          password='65306565',
                                          database='xiaohuabase',
                                          charset='UTF8',

                                          )

        conn = pool.connection()
        # 可以增加autocommit
        cmd = conn.cursor()

        cmd.execute(query=SQL)
        conn.commit()

        print('更新影响行数%s' % cmd.rowcount)
    except Exception:
        conn.rollback()

        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    main()
