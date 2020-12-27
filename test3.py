import traceback, pymysql

'''SQL = "SELECT uid,name,age,birthday,salary,note FROM user "'''   #写*要被扣工资
SQL="SELECT uid,name,age,birthday,salary,note FROM user WHERE uid=%s"


def main():
    try:
        conn = pymysql.connect(host='localhost', port=3306, charset='UTF8', user='root', password='65306565',
                               database='xiaohuabase')
        cmd = conn.cursor()
        cmd.execute(query=SQL,args=[1])

        for user_row in cmd.fetchall(): #返回全部
            uid=user_row[0]
            name=user_row[1]
            age=user_row[2]
            birthday=user_row[3]
            salary=user_row[4]
            note=user_row[5]
            print('用户id%s 用户名字%s'%(uid,name))




        print('更新影响行数%s'% cmd.rowcount)

    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    main()
