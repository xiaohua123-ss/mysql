import traceback, pymysql
name='xiaohuau'
age=15
birthday='2020-01-05'
salary=5000
note='eat'
'''SQL = "SELECT uid,name,age,birthday,salary,note FROM user "'''   #写*要被扣工资
SQL="INSERT INTO user(name,age,birthday,salary,note) VALUES(%s,%s,%s,%s,%s)"


def main():
    try:
        conn = pymysql.connect(host='localhost', port=3306, charset='UTF8', user='root', password='65306565',
                               database='xiaohuabase')
        cmd = conn.cursor()
        cmd.execute(query=SQL,args=[name,age,birthday,salary,note])
        conn.commit()
        print('更新影响%s'%cmd.rowcount)






        print('更新影响行数%s'% cmd.rowcount)

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    main()