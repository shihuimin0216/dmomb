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
        cook = self.get_arguments("opcookie")
        print(type(cook), cook)
        if cook == ['off']:
            print(cook)
            self.clear_cookie("current_username")
<<<<<<< HEAD
       # loader = Template
        print("view_index.py")
        # time.sleep(5)
        self.html(os.path.join(configs['templates_path'], 'shouye/index.html'))
=======
        print("程序访问到view_index.py")
        # 数据模块的访问所有数据
        service = Service_index()
        datas = service.get_10_data

        # 模型模块访问批量数据
        models = service.get_10_model

        # 硬件模块访问批量数据
        machine = service.get_10_machine
        self.html(os.path.join(
            configs['templates_path'], 'shouye/index.html'), data=datas, models=models, machine=machine)
>>>>>>> 99d4170b707cfbe9ea2b30f825d14ff558b6fa85
