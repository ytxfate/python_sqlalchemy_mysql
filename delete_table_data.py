#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  delete_table_data.py
@Desc :  删除
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules
from model import Emp


class DeleteTableData:
    """
    删除
    """
    def __init__(self, session):
        self.session = session
    
    def delete_data(self):
        """
        删除
        """
        self.session.query(Emp).filter(Emp.emp_id==2).delete()
        self.session.commit()
    
    def main(self):
        """
        主函数
        """
        self.delete_data()
    

