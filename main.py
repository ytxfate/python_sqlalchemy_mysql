#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  main.py
@Desc :  主测试文件
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
# User-defined Modules
from init_conn import InitConn
from model import Base

from query_table_data import QueryTableData
from add_table_data import AddTableData
from update_table_data import UpdateTableData
from delete_table_data import DeleteTableData


if __name__ == '__main__':
    engine = InitConn().get_engine()
    SessionFactory = sessionmaker(bind=engine)
    # 生成 session：
    # 方式一：
    session = scoped_session(SessionFactory)    # 当使用 scoped_session 时，用 session.remove() 关闭 session
    # 方式二：
    # session = SessionFactory()                  # 当使用 scoped_session 时，用 session.close() 关闭 session


    # # 1 删除表
    # Base.metadata.drop_all(engine)
    # # 2 创建表
    # Base.metadata.create_all(engine)

    # # 3 查询
    # QueryTableData(session).main()
    # # 4 新增
    # AddTableData(session).main()
    # # 5 修改
    # UpdateTableData(session).main()
    # # 6 删除
    # DeleteTableData(session).main()
    
    # 关闭 session
    session.remove()
