import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm
import sqlalchemy.orm.session
import datetime

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
    bir_date = datetime.datetime.strptime("2015-10-6", "%Y-%m-%d")
    user = User(uid=2,name='小白', age=999, birthday=bir_date, salary=1.0, note='aaaaaa')
    session.merge(user)
    session.commit()


    print(user)
    session.close()


if __name__ == "__main__":
    main()
