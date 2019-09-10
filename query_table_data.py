#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  query_table_data.py
@Desc :  查询
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from sqlalchemy.sql import text
from sqlalchemy import and_, or_
# User-defined Modules
from model import Emp, Dept


class QueryTableData:
    """
    查询
    """
    def __init__(self, session):
        self.session = session

    def query_data_01(self):
        # 1 全字段全数据
        rows = self.session.query(Emp).all()
        for row in rows:
            print(row.emp_id, row.emp_name)
        # 2 部分字段第一行数据
        r2 = self.session.query(Emp.emp_id, Emp.emp_name).first()
        print(r2)
        # 3 条件查询
        r3 = self.session.query(Emp.emp_id, Emp.emp_name).filter(Emp.emp_id==1).first()
        print(r3)
        # 4 模糊查询
        r4 = self.session.query(Emp.emp_id, Emp.emp_name).filter(Emp.emp_name.like("%三%")).first()
        print(r4)
        # 5 改变字段名
        r5 = self.session.query(
            Emp.emp_id.label('id'), Emp.emp_name.label('name')
        ).filter(Emp.emp_name.like("%三%")).first()
        print(r5.id, r5.name)
        # 6 使用 sql 语句
        r6 = self.session.query(Emp).from_statement(
            text("SELECT * FROM emp where emp_name=:emp_name")
        ).params(emp_name='张三').first()
        print(r6.emp_id, r6.emp_name)
        # 7 组装
        r7 = self.session.query(Emp).filter(
            text("emp_id<=:emp_id and emp_name=:emp_name")
        ).params(emp_id=1, emp_name='张三').order_by(Emp.emp_id).first()
        print(r7.emp_id, r7.emp_name)
        # 8 in
        rows8 = self.session.query(Emp).filter(Emp.emp_id.in_([1,3,4])).all()
        for row81 in rows8:
            print(row81.emp_id, row81.emp_name)
        # 9 between
        rows9 = self.session.query(Emp).filter(Emp.emp_id.between(1, 3)).all()
        for row91 in rows9:
            print(row91.emp_id, row91.emp_name)
        # 10 and
        r10 = self.session.query(Emp.emp_id, Emp.emp_name).filter(
            and_(Emp.emp_id==1, Emp.emp_name=='张三')
        ).first()
        print(r10)
        # 11 or
        r11 = self.session.query(Emp.emp_id, Emp.emp_name).filter(
            or_(Emp.emp_id==3, Emp.emp_name=='张三')
        ).first()
        print(r11)
        # 12 非
        r12 = self.session.query(Emp).filter(~Emp.emp_id.in_([1,2,4])).first()
        print(r12.emp_id, r12.emp_name)
        # 13 sql
        cursor = self.session.execute(
            'select * from emp where emp_id=:emp_id', params={"emp_id": 1}
        )
        r13s = cursor.fetchall()
        for r13 in r13s:
            print(r13)

    def query_data_02(self):
        # 1 多表查询
        # 1.1 方式1：
        r11 = self.session.query(Emp).filter(
            Emp.emp_id.in_(self.session.query(Emp.emp_id).filter_by(emp_name='张三'))
        ).first()
        print(r11.emp_id, r11.emp_name)
        # 1.2 方式2：
        r12 = self.session.query(Emp, Dept).filter(Emp.dept_id == Dept.dept_id).first()
        print(r12[0].emp_name, r12[1].dept_name)
        # 1.3 方式3：
        r13s = self.session.query(Emp).join(Dept).all()
        for r13 in r13s:
            print(r13)
        # 1.4 方式4：
        r14s = self.session.query(Emp).join(Dept, isouter=True).all()
        for r14 in r14s:
            print(r14.emp_name)
        # 2 union
        q1 = self.session.query(Emp.emp_id, Emp.emp_name).filter(Emp.emp_id >= 1)
        q2 = self.session.query(Dept.dept_id, Dept.dept_name).filter(Dept.dept_id >= 1)
        r2s = q1.union(q2).all()
        for r2 in r2s:
            print(r2)
        # 3 union_all
        q1 = self.session.query(Emp.emp_id, Emp.emp_name).filter(Emp.emp_id >= 1)
        q2 = self.session.query(Dept.dept_id, Dept.dept_name).filter(Dept.dept_id >= 1)
        r2s = q1.union_all(q2).all()
        for r2 in r2s:
            print(r2)



    def main(self):
        """
        主函数
        """
        self.query_data_01()
        self.query_data_02()
    
