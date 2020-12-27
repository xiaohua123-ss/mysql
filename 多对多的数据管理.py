import datetime

import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm
import sqlalchemy.orm.session

MYSQL_URL = "mysql+mysqlconnector://root:65306565@localhost:3306/xiaohuabase"
Base = sqlalchemy.ext.declarative.declarative_base()
user_role = sqlalchemy.Table("user_role", Base.metadata,
                             sqlalchemy.Column("uid", sqlalchemy.String, sqlalchemy.ForeignKey("user.uid"),
                                               nullable=False, primary_key=True),
                             sqlalchemy.Column("rid", sqlalchemy.String, sqlalchemy.ForeignKey("role.rid"),
                                               nullable=False, primary_key=True))


# 父类类型 <class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'>
class User(Base):  # <class 'sqlalchemy.ext.declarative.api.Base'>
    __tablename__ = 'user'
    uid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    roles = sqlalchemy.orm.relationship("Role", secondary=user_role, backref="user")

    def __repr__(self):
        return "用户ID %s，姓名%s" % (self.uid, self.name)


class Role(Base):
    __tablename__ = "role"
    rid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return "角色ID %s，名称%s" % (self.rid, self.title)


def main():
    engine = sqlalchemy.create_engine(MYSQL_URL, encoding='UTF8', echo=True)
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建sesstion类型
    session = sqlalchemy.orm.session.Session()

    #user = User(uid='python', name='小李老师', roles=roles)
    user=session.query(User).get("yootk")
    print(user)
    for role in user.roles:
        print("\t%s"%role)

    #session.add(user)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
