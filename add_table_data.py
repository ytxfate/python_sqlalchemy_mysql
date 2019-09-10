#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  add_table_data.py
@Desc :  新增
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules
from model import Emp, Dept, Student, Course, Student2Course


class AddTableData:
    """
    新增
    """
    def __init__(self, session):
        self.session = session
    
    def single_table_add_data(self):
        """
        单表新增
        """
        self.session.add(
            Dept(dept_name="开发")
        )
        # self.session.commit()
        self.session.add_all([
            Dept(dept_name="销售"),
            Dept(dept_name="运营"),
            Dept(dept_name="宣传")
        ])
        self.session.commit()
    
    def one_to_many_table_add_data(self):
        """
        一对多表新增
        """
        dept_1 = Dept(dept_name="Python")
        dept_2 = Dept(dept_name='Java')
        dept_1.emp_list = [
            Emp(emp_name='张三'),
            Emp(emp_name='李四')
        ]
        dept_2.emp_list = [
            Emp(emp_name='王二')
        ]
        self.session.add_all([dept_1, dept_2])
        self.session.commit()
    
    def many_to_many_table_add_data(self):
        """
        多对多表新增
        """
        course_1 = Course(course_name='语文')
        course_2 = Course(course_name='数学')
        course_1.student_list = [
            Student(student_name="张三"),
            Student(student_name="李四"),
        ]
        course_2.student_list = [
            Student(student_name="王二")
        ]
        self.session.add_all([course_1, course_2])
        self.session.commit()

    def main(self):
        """
        主函数
        """
        # 单表新增
        self.single_table_add_data()
        # 一对多表新增
        self.one_to_many_table_add_data()
        # 多对多表新增
        self.many_to_many_table_add_data()
    
