import sqlalchemy
import sqlalchemy.ext.declarative  # 父类的结构定义
import sqlalchemy.orm
import sqlalchemy.orm.session
import datetime

MYSQL_URL = "mysql+mysqlconnector://root:65306565@localhost:3306/xiaohuabase"

Base = sqlalchemy.ext.declarative.declarative_base()


# 父类类型 <class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'>
class Company(Base):  # <class 'sqlalchemy.ext.declarative.api.Base'>
    __tablename__ = 'company'  # 映射表
    cid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    cname = sqlalchemy.Column(sqlalchemy.String)
    site = sqlalchemy.Column(sqlalchemy.String)
    depts=sqlalchemy.orm.relationship('Dept',order_by="Dept.cid",backref="company")

    def __repr__(self):
        return "公司编号:%s,名称：%s,网址%s" % (self.cid, self.cname, self.site)


class Dept(Base):
    __tablename__ = 'dept'
    did = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True)
    dname = sqlalchemy.Column(sqlalchemy.String)
    cid = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("company.cid"))

    def __repr__(self) -> str:
        return "部门编号%s,名称 %s,公司编号%s" % (self.did,self.dname,self.cid)


def main():
    engine = sqlalchemy.create_engine(MYSQL_URL, encoding='UTF8', echo=True)
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)  # 创建sesstion类型

    #1.dept_list=[Dept(dname="软件部"),Dept(dname="信息部"),Dept(dname="客服部")]
    #1.company=Company(cid="c-002",cname='xiaohua',site='www.xiaohua.com',depts=dept_list)
    session = sqlalchemy.orm.session.Session()
    company=session.query(Company).join(Dept).filter(Company.cid==Dept.cid).filter(Company.cid=="C-001").filter(
        Dept.dname=="教材研发部").one()
    print(company)
    print(company.depts)
    #3.company=session.query(Company).get("C-001")
    #print(company)
    #print(company.depts)
    #2.dept=Dept(dname="测试部",cid="c-002')
    #2.session.add(kept)


    '''session.add(company)
    session.commit()
    for dept in dept_list:
        print("新增部门编号did=%s"%dept.did)'''


    session.close()


if __name__ == "__main__":
    main()
