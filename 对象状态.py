import sqlalchemy, sqlalchemy.ext.declarative, sqlalchemy.orm, sqlalchemy.orm.session
MYSQL_URL = "mysql+mysqlconnector://root:65306565@localhost:3306/xiaohuabase"
class User(sqlalchemy.ext.declarative.declarative_base()):  # 定义数据表映射类
    __tablename__ = "user"  # 映射表名称
    uid = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True)  # 映射user.uid字段
    name = sqlalchemy.Column(sqlalchemy.String)  # 映射user.name字段
    age = sqlalchemy.Column(sqlalchemy.Integer)  # 映射user.age 字段
    birthday = sqlalchemy.Column(sqlalchemy.Date)  # 映射user.birthday字段
    salary = sqlalchemy.Column(sqlalchemy.Float)  # 映射user.salary字段
    note = sqlalchemy.Column(sqlalchemy.String)  # 映射user.note字段
    def __repr__(self) -> str:  # 对象输出
        return "用户编号：%s、姓名：%s、年龄：%s、生日：%s、月薪：%s、备注：%s" % \
               (self.uid, self.name, self.age, self.birthday, self.salary, self.note)
def main():  # 主函数
    engine = sqlalchemy.create_engine(MYSQL_URL, encoding="utf8", echo=True)  # 数据库引擎
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建Session
    session_A = sqlalchemy.orm.session.Session()# 实例化Session
    session_B=sqlalchemy.orm.session.Session()
    user=session_A.query(User).get(2025)#变为持久
    session_A.close()#游离态 从session消失了
    user=session_B.query(User).get(2025) #游离态变为持久态
    user.name='aaa'
    user.age=888
    session_B.merge(user)
    session_B.commit()
    session_B.close()




if __name__ == "__main__":  # 判断执行名称
    main()  # 调用主函数

