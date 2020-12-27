import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm
import sqlalchemy.orm.session
import datetime
#不适合过于繁琐的过程
MYSQL_URL = "mysql+mysqlconnector://root:65306565@localhost:3306/xiaohuabase"


# 父类类型 <class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'>
class User(sqlalchemy.ext.declarative.declarative_base()):  # <class 'sqlalchemy.ext.declarative.api.Base'>
    __tablename__ = 'user'
    uid = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    birthday = sqlalchemy.Column(sqlalchemy.Date)
    salary = sqlalchemy.Column(sqlalchemy.Float)
    note = sqlalchemy.Column(sqlalchemy.Text)

    def __repr__(self) -> str:
        return "用户编号: %s，姓名: %s,年龄 %s,生日 %s,月薪 %s 备注 %s" % \
               (self.uid, self.name, self.age, self.birthday, self.salary, self.note)


def main():
    engine = sqlalchemy.create_engine(MYSQL_URL, encoding='UTF8', echo=True)
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建sesstion类型
    session = sqlalchemy.orm.session.Session()

    # 根据ID查询有默认额实现 session.query(User).get(1)
    #user_list = session.query(User).filter(User.name.like("%小花%")).slice(0,1).all()
    # 返回了一个列表  offset(0).limit(1). 第几个  ，总共几个

    user_list=session.query(User).filter(User.uid.in_([1090,1100])).all()
    #数量计算
    user_count=session.query(sqlalchemy.func.count(User.uid)).one()
    print(user_list)
    print(user_count)
    session.close()


if __name__ == "__main__":
    main()
