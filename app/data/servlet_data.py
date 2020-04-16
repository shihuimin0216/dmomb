# _*_ coding: utf-8 _*_
from app.data.dbManage_data import dbManage


class Servlet_data:
    def __init__(self, data):
        self.db = dbManage()
        self.data = data
    # 将data类转化为字典
    @property
    def dict_data(self):
        return dict(
            self.data
        )

    # 处理数据,并插入数据库
    def process_data(self, user_uuid):
        print(self.dict_data)
        # 将数据插入数据库
        data_flag = self.db.insert(self.dict_data)
        # 将数据和用户的连接插入数据库
        user_data_flag = self.db.insert_user_data(
            data_uuid=self.dict_data['uuid'],
            user_uuid=user_uuid
        )
        if data_flag and user_data_flag:
            return True
        return False
        # 将数据库中的数据全部显示出来

    def show_all(self):
        # 做一些查询之前的处理,例如用户信息的验证等等
        data = dict(
            collections=self.db.find_all()
        )
        print(data)
        return data
