import traceback, pymysql

SQL = "SELECT uid,name,age,birthday,salary,note FROM user WHERE name LIKE %s LIMIT %s,%s"


def main():
    keyword='%沐言%'
    current_page=1   #LIMIT 第一个参数 是第几个满足条件的 第二个参数是记录个数

    line_size=2
    try:
        conn = pymysql.connect(host="localhost", port=3306, charset='UTF8', user='root', password='65306565',
                               database='xiaohuabase')
        cmd=conn.cursor()
        cmd.execute(query=SQL,args=[keyword,(current_page-1)*line_size,line_size])
        for user_row in cmd.fetchall():
            uid=user_row[0]
            name=user_row[1]
            age=user_row[2]
            birthday=user_row[3]
            salary=user_row[4]
            note=user_row[5]
            print('用户ID： %s,姓名:%s,年龄：%s,生日%s'%(uid,name,age,birthday))
    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    main()
