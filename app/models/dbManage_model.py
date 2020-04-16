# _*_ coding: utf-8 _*_
from app.common.MDConnector import MDConnector


class dbManage_model(MDConnector):  # 继承公共数据库连接器
    # def __init__(self):
    #     self.co = self.db.data_info
    # 将数据字典插入,如果插入成功返回True,如果插入失败,返回False

    def insert(self, dict_form):
        self.co = self.db.model_info
        # print(dict_form)
        inser_flag = self.co.insert_one(
            dict_form
        )
        if not inser_flag:
            return True
        return False

    def insert_user_model(self, model_uuid, user_uuid):
        # 获取插入集合的链接
        self.co = self.db.user_model_info
        # 将其处理成字符串进行插入
        insert_flag = self.co.insert_one(
            dict(
                model_uuid=model_uuid,
                user_uuid=user_uuid
            )
        )
        if not insert_flag:
            return True
        return False

    # 查找全部数据库的数据

    def find_all(self):
        # 获取集合
        self.co = self.db.model_info
        # 查找集合的所以元素
        result = self.co.find()
        return result
