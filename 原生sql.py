import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm
import sqlalchemy.orm.session
import datetime
#不适合过于繁琐的过程
MYSQL_URL = "mysql+mysqlconnector://root:65306565@localhost:3306/xiaohuabase"
SQL="DELETE FROM user WHERE uid=:uid"





def main():
    engine = sqlalchemy.create_engine(MYSQL_URL, encoding='UTF8', echo=True)
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建sesstion类型
    session = sqlalchemy.orm.session.Session()
    result=session.execute(SQL,{"uid":1})
    print('删除的行数%s'%result.rowcount)
    session.commit()
    session.close()



    session.close()


if __name__ == "__main__":
    main()
