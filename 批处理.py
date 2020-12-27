import traceback, pymysql
name='xiaohuau'
age=15
birthday='2020-01-05'
salary=5000
note='eat'

SQL="INSERT INTO user(name,age,birthday,salary,note) VALUES(%s,%s,%s,%s,%s)"


def main():
    try:
        conn = pymysql.connect(host='localhost', port=3306, charset='UTF8', user='root', password='65306565',
                               database='xiaohuabase')
        cmd = conn.cursor()
        data_list=[]
        for num in range(1001):
            data_list.append(('小花%s号'%num,18,'2008-10-19','5000','chi'))
            if num%20==0:
                cmd.executemany(query=SQL,args=data_list)
                data_list.clear()



        conn.commit()


    except Exception:
        print(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    main()
