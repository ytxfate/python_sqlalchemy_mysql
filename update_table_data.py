#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  update_table_data.py
@Desc :  修改
'''

# The Python Standard Modules(Library) and Third Modules(Library)
import datetime
# User-defined Modules
from model import Emp


class UpdateTableData:
    """
    修改
    """
    def __init__(self, session):
        self.session = session
    
    def update_data(self):
        """
        修改
        """
        self.session.query(Emp).filter(Emp.emp_id==1).update({'birthday': datetime.datetime.now()})
        self.session.commit()
    
    def main(self):
        """
        主函数
        """
        self.update_data()
    
