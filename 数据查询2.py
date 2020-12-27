import sqlalchemy, sqlalchemy.ext.declarative, sqlalchemy.orm, sqlalchemy.orm.session

MYSQL_URL = "mysql+mysqlconnector://root:65306565@localhost:3306/xiaohuabase"
import random
SQL="SELECT uid,name,note FROM  LIMIT :start,:size"



def main():  # 主函数
    engine = sqlalchemy.create_engine(MYSQL_URL, encoding="utf8", echo=True)  # 数据库引擎
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建Session
    session = sqlalchemy.orm.session.Session()
    result=session.execute(SQL,[{"start":0,"size":20}])
    for  row in result.fetchall():
        print(row)

    session.close()


if __name__ == "__main__":  # 判断执行名称
    main()  # 调用主函数
