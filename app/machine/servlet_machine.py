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
    def process_machine(self, user_uuid):
        print(self.dict_machine)
        # 将数据插入数据库
        machine_flag = self.db.insert(self.dict_machine)
        # 将数据和用户的连接插入数据库
        user_machine_flag = self.db.insert_user_machine(
            machine_uuid=self.dict_machine['uuid'],
            user_uuid=user_uuid
        )
        if machine_flag and user_machine_flag:
            return True
        return False
    # 将数据库中的数据全部显示出来

    def show_all(self):
        # 做一些查询之前的处理,例如用户信息的验证等等
        machines = dict(
            collections=self.db.find_all()
        )
        print(machines)
        return machines

    # 根据用户信息查询用户有那些machine
    def show_zone_all(self, user_uuid):
        machine = dict(
            collections=self.db.find_zone_all(user_uuid)
        )
        return machine
