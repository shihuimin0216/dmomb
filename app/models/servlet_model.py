# _*_ coding: utf-8 _*_
from app.models.dbManage_model import dbManage_model


class Servlet_model:
    def __init__(self, model):
        self.db = dbManage_model()
        self.model = model
    # 将模型类转化为字典
    @property
    def dict_model(self):
        return dict(
            self.model
        )

    # 处理数据,并插入数据库
    # 处理数据,并插入数据库
    def process_model(self, user_uuid):
        print(self.dict_model)
        # 将数据插入数据库
        model_flag = self.db.insert(self.dict_model)
        # 将数据和用户的连接插入数据库
        user_model_flag = self.db.insert_user_model(
            model_uuid=self.dict_model['uuid'],
            user_uuid=user_uuid
        )
        if model_flag and user_model_flag:
            return True
        return False
    # 将数据库中的数据全部显示出来

    def show_all(self):
        # 做一些查询之前的处理,例如用户信息的验证等等
        models = dict(
            collections=self.db.find_all()
        )
        print(models)
        return models
