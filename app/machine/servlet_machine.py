# _*_ coding: utf-8 _*_
from app.machine.dbManage_machine import dbManage_machine


class Servlet_machine:
    def __init__(self, machine):
        self.db = dbManage_machine()
        self.machine = machine
    # 将模型类转化为字典
    @property
    def dict_machine(self):
        return dict(
            self.machine
        )

    # 处理数据,并插入数据库
    def process_machine(self):
        print(self.dict_machine)
        # 插入数据库
        return self.db.insert(
            self.dict_machine
        )
    # 将数据库中的数据全部显示出来

    def show_all(self):
        # 做一些查询之前的处理,例如用户信息的验证等等
        machines = dict(
            collections=self.db.find_all()
        )
        print(machines)
        return machines
