# _*_ coding: utf-8 _*_
import time
import os
import tornado.gen
import tornado.concurrent
from app.api.view_common import CommonHandler
from app.configs import configs
from tornado.escape import utf8
from tornado.util import unicode_type
from app.api.service_index import Service_index


class IndexHandler(CommonHandler):
    # executor = ThreadPoolExecutor(50)
    # get
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.write("这是管理员后台系统")
