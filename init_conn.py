#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  init_conn.py
@Desc :  初始化数据库连接
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from sqlalchemy import create_engine
# User-defined Modules

class InitConn:
    """
    初始化数据库连接
    """
    def __init__(self):
        conn_base_str = "{driver}://{username}:{password}@{host_port}/{database}{parameter}"
        conn_param = {
            'driver': 'mysql+mysqlconnector',
            'username': 'user',
            'password': 'user',
            'host_port': '127.0.0.1:3306',
            'database': 'study',
            'parameter': '?auth_plugin=mysql_native_password&charset=utf8',
        }
        self.engine = create_engine(
            conn_base_str.format_map(conn_param),
            max_overflow=0,     # 超过连接池大小外最多创建的连接
            pool_size=5,        # 连接池大小
            pool_timeout=30,    # 池中没有线程最多等待的时间，否则报错
            pool_recycle=-1     # 多久之后对线程池中的线程进行一次连接的回收（重置）
        )
    
    def get_engine(self):
        """
        获取数据库连接初始化结果
        """
        return self.engine
