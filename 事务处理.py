import traceback

import pymysql

SQL_A = "INSERT INTO user(name, note) VALUES('小李', 'aaa')"
SQL_B = "INSERT INTO user(name, note) VALUES('小'l', 'aaa')"
SQL_C = "INSERT INTO user(name, note) VALUES('小C', 'aaa')"


def main():
    try:
        conn = pymysql.connect(host='localhost', port=3306, charset='UTF8', user='root', password='65306565',
                               database='xiaohuabase')
        # 可以增加autocommit
        cmd = conn.cursor()
        conn.autocommit(False)

        cmd.execute(query=SQL_A)
        cmd.execute(query=SQL_B)
        cmd.execute(query=SQL_C)

        print('更新影响行数%s' % cmd.rowcount)
    except Exception:
        conn.rollback()

        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    main()
