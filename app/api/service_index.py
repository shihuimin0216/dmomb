# _*_ coding: utf-8 _*_

from app.data.servlet_data import Servlet_data
from app.models.servlet_model import Servlet_model


class Service_index:
    def __init__(self):
        pass

    # 读取前10个模型样例
    @property
    def get_10_data(self):
        data_service = Servlet_data(None)
        # 暂时使用查询全部,以后数据多起来了,要改为查询前30个
        data = data_service.show_all()
        return data
    # 读取前30个数据样例
    @property
    def get_10_model(self):
        model_service = Servlet_model(None)
        # 暂时使用查询全部,以后数据多起来了,要改为查询前30个
        models = model_service.show_all()
        return models
    # 读取前30个工具样例

    def get_10_mechile(self):
        pass
