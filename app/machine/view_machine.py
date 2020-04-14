# _*_ coding: utf-8 _*_
import os
import datetime
import json
import markdown
import codecs

import tornado.gen
import tornado.concurrent

from bson.objectid import ObjectId
from app.api.html_common import HtmlHandler
from app.configs import configs
from app.common.forms import MachineForm
from app.machine.Machine import Machine
from app.machine.servlet_machine import Servlet_machine
# 显示机械相关信息


class MachineHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # print("curent_username", self.get_secure_cookie("current_username"))
        # # 添加servlet进行出来
        servlet = Servlet_machine(None)
        # 读取数据
        machine = servlet.show_all()
        self.html(os.path.join(
            configs['templates_path'], 'machine/machine.html'), data=machine)

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True

# 添加model相关信息


class AddMachineHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'machine/add_machine.html'))

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        file_metas = self.request.files.get('file', None)
        # 对表单进行验证
        form = MachineForm(self.form_params)
        print("view_machine的:", self.form_params)
        if form.validate():
            print(self.get_secure_cookie('jupyter_path', None))
            # 实例化这个data类
            machine = Machine(
                name=form.data['name'],
                paper=form.data['paper'],
                data_url=form.data['data_url'],
                file_path=self.get_secure_cookie('file_db', None),
                jupyter_path=self.get_secure_cookie('jupyter_path', None),
                img_path=self.get_secure_cookie('image_path', None),
                info=form.data['markdown'],
                createAt=datetime.datetime.now(),
                updatedAt=datetime.datetime.now()
            )
            # 将数据传给servlet处理
            servlet = Servlet_machine(
                machine
            )
            if servlet.process_machine():
                # 数据处理成功
                res['code'] = 1
                res['msg'] = '成功'
            else:
                res['code'] = 0
                res['msg'] = '数据库格式要求不符合'
        else:
            # 定义失败接口格式
            res['data'] = form.errors
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True


# 模型详情信息显示渲染


class MachineDetail(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        _id = str(self.get_argument('_id'))
        print(_id)
        db = self.md.dmomb
        co = db.machine_info
        collections = co.find({'_id': ObjectId(_id)})
        # 加一步将markdown转化为html文件.
        css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
            <!-- 此处省略掉markdown的css样式，因为太长了 -->
            </style>
            '''
        # html = css + markdown.markdown(collections[0]['markdown_info'])
        #################
        data = dict(
            collection=collections[0]
        )
        print("view_machine.py", data)
        self.html(os.path.join(
            configs['templates_path'], 'machine/machine_detail.html'), data=data)

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True
