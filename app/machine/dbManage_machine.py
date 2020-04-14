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
    # 查找全部数据库的数据

    def find_all(self):
        # 获取集合
        self.co = self.db.machine_info
        # 查找集合的所以元素
        result = self.co.find()
        return result
