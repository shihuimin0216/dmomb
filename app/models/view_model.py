# _*_ coding: utf-8 _*_
import os
import datetime
import json
import markdown
import codecs
import uuid
import tornado.gen
import tornado.concurrent

from bson.objectid import ObjectId
from app.api.html_common import HtmlHandler
from app.configs import configs
from app.common.forms import ModelForm
from app.models.Model import Model
from app.models.servlet_model import Servlet_model
# 显示model相关信息


class ModelHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        print("curent_username", self.get_secure_cookie("current_username"))
        # 添加servlet进行出来
        servlet = Servlet_model(None)
        # 读取数据
        model = servlet.show_all()
        self.html(os.path.join(
            configs['templates_path'], 'models/model.html'), data=model)

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


class AddModelHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'models/add_model.html'))

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        file_metas = self.request.files.get('file', None)
        # 对表单进行验证
        form = ModelForm(self.form_params)
        if form.validate():
            print(self.get_secure_cookie('jupyter_path', None))
            # 实例化这个data类
            model = Model(
                uuid=uuid.uuid4(),
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
            servlet = Servlet_model(
                model
            )
            user_uuid = self.get_secure_cookie('uuid', None)
            if servlet.process_model(user_uuid):
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


class ModelDetail(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        print("进入页面信息")
        _id = str(self.get_argument('_id'))
        print(_id)
        db = self.md.dmomb
        co = db.model_info
        collections = co.find({'_id': ObjectId(_id)})
        print(collections)
        # 加一步将markdown转化为html文件.
        css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
            <!-- 此处省略掉markdown的css样式，因为太长了 -->
            </style>
            '''
        # html = css + markdown.markdown(collections[0]['markdown_info'])
        #################
        # print(collections[0])
        data = dict(
            collection=collections[0]
        )

        self.html(os.path.join(
            configs['templates_path'], 'models/model_detail.html'), data=data)

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
