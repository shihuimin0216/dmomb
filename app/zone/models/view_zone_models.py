# _*_ coding: utf-8 _*_
import os
import uuid
import datetime
import markdown
import tornado.gen
import tornado.concurrent

from app.api.html_common import HtmlHandler
from app.configs import configs
from app.models.Model import Model
from bson.objectid import ObjectId
from app.models.servlet_model import Servlet_model

#


class ZoneModelsHandler(HtmlHandler):
    '''
        功能介绍, 数据库中存储的数据信息,显示到一个页面上, 就像淘宝的商品一样,
        这个类主要用于数据的读取并回传到前端
    '''
    # 将数据从数据库读取, 并且返回
    @tornado.gen.coroutine
    def get(self):

        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # 获取当前用户的uuid
        user_uuid = self.get_secure_cookie("uuid", None)

        # 添加servlet进行出来
        servlet = Servlet_model(None)
        # # 读取数据
        models = servlet.show_zone_all(user_uuid)

        # 渲染数据到页面
        self.html(os.path.join(
            configs['templates_path'], 'zone/zone_datas.html'), data=models)
