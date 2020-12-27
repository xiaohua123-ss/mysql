import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm
import sqlalchemy.orm.session
import  datetime
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

    pass


def main():
    engine = sqlalchemy.create_engine(MYSQL_URL,encoding='UTF8',echo=True)
    sqlalchemy.orm.session.Session=sqlalchemy.orm.sessionmaker(bind=engine)  #创建sesstion类型
    session=sqlalchemy.orm.session.Session()
    bir_date=datetime.datetime.strptime("2015-11-6","%Y-%m-%d")
    user=User(name='小李',age=15,birthday=bir_date,salary=2400,note='aaaaaa')
    #user.name=''xiao白 可以更改数据
    session.add(user)   #sql处理(orm）转换
    session.commit()
    print('数据保存成功,当前ID为%s'%user.uid)
    session.close()


if __name__ == "__main__":
    main()