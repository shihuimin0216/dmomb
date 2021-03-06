# _*_ coding: utf-8 _*_
from app.common.MDConnector import MDConnector


class dbManage_machine(MDConnector):  # 继承公共数据库连接器
    # def __init__(self):
    #     self.co = self.db.data_info
    # 将数据字典插入,如果插入成功返回True,如果插入失败,返回False

    def insert(self, dict_form):
        self.co = self.db.machine_info
        # print(dict_form)
        inser_flag = self.co.insert_one(
            dict_form
        )
        if not inser_flag:
            return True
        return False

    def insert_user_machine(self, machine_uuid, user_uuid):
        # 获取插入集合的链接
        self.co = self.db.user_machine_info
        # 将其处理成字符串进行插入
        insert_flag = self.co.insert_one(
            dict(
                machine_uuid=machine_uuid,
                user_uuid=user_uuid
            )
        )
        if not insert_flag:
            return True
        return False

    # 查找全部数据库的数据

    def find_all(self):
        # 获取集合
        self.co = self.db.machine_info
        # 查找集合的所以元素
        result = self.co.find()
        return result

    # 查找指定uuid的用户所以的数据
    def find_zone_all(self, user_uuid):
        machine_lists = []
        self.user_machine = self.db.user_machine_info
        self.machine = self.db.machine_info
        # 第一步将该用户拥有的所以数据的uuid查询出来
        result_user_machines = self.user_machine.find({'user_uuid': user_uuid})

        # 第二部将每个用户machine的具体信息进行封装
        for v in result_user_machines:
            print(v['machine_uuid'])
            machine = self.machine.find({
                'uuid': v['machine_uuid']  # 根据machine的uuid查询信息
            })
            # 将信息添加到一个list当中,由于查询machine是一个cursor,需要指定为0下标
            machine_lists.append(machine[0])

        result = machine_lists
        print(result)
        return result
