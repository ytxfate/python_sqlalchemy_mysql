#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  model.py
@Desc :  orm 模型
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import relationship
# User-defined Modules


Base = declarative_base()
# ================================== 一对多 ================================== #
class Emp(Base):
    __tablename__ = 'emp'

    emp_id = Column(Integer, primary_key=True, autoincrement=True)
    emp_name = Column(String(20), nullable=False)
    birthday = Column(Date)
    sex = Column(Integer)

    # 外键
    dept_id = Column(Integer, ForeignKey('dept.dept_id'))
    # 关系
    dept = relationship('Dept', backref='emp_list')


class Dept(Base):
    __tablename__ = 'dept'

    dept_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(50), nullable=False)

    __table_args__ = (
        UniqueConstraint('dept_id', 'dept_name', name='dept_id_name'),
    )

# ================================== 多对多 ================================== #
class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(20), nullable=False)

    # 关系
    course_list = relationship('Course', secondary='student2course', backref='student_list')

class Course(Base):
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(20), nullable=False)

class Student2Course(Base):
    __tablename__ = 'student2course'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.student_id'))
    course_id = Column(Integer, ForeignKey('course.course_id'))
