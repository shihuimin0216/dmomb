# _*_ coding: utf-8 _*_
import os
import uuid
import datetime
import markdown
import tornado.gen
import tornado.concurrent

from app.api.html_common import HtmlHandler
from app.configs import configs
from app.common.forms import DataForm
from app.data.Data import Data
from bson.objectid import ObjectId
from app.data.servlet_data import Servlet_data

#


class DataHandler(HtmlHandler):
    '''
        功能介绍, 数据库中存储的数据信息,显示到一个页面上, 就像淘宝的商品一样,
        这个类主要用于数据的读取并回传到前端
    '''
    #将数据从数据库读取, 并且返回
    @tornado.gen.coroutine
    def get(self):

        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # 添加servlet进行出来
        servlet = Servlet_data(None)
        # 读取数据
        data = servlet.show_all()
        # 渲染数据到页面
        self.html(os.path.join(
            configs['templates_path'], 'data/data.html'), data=data)


# 上传文件
class DataUploadHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'data/upload_data.html'))

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        file_metas = self.request.files.get('file', None)
        # 对表单进行验证
        form = DataForm(self.form_params)
        if form.validate():
            print(self.get_secure_cookie('jupyter_path', None))
            # 实例化这个data类
            data = Data(
                uuid=uuid.uuid4(),
                name=form.data['name'],
                file_path=self.get_secure_cookie('file_db', None),
                jupyter_path=self.get_secure_cookie('jupyter_path', None),
                img_path=self.get_secure_cookie('image_path', None),
                info=form.data['markdown'],
                createAt=datetime.datetime.now(),
                updatedAt=datetime.datetime.now()
            )
            # 将数据传给servlet处理
            servlet = Servlet_data(
                data=data
            )
            user_uuid = self.get_secure_cookie('uuid', None)
            if servlet.process_data(user_uuid):
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


# 模型数据详情信息显示渲染


class DataDetail(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        _id = str(self.get_argument('_id'))
        print(_id)
        db = self.md.dmomb
        co = db.data_info
        collections = co.find({'_id': ObjectId(_id)})
        # 加一步将markdown转化为html文件.
        css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
            <!-- 此处省略掉markdown的css样式，因为太长了 -->
            </style>
            '''
        # markdown_info = markdown.markdown(collections[0]['info'])

        #################
        print(collections[0])
        data = dict(
            collection=collections[0]
        )
        print(data)
        self.html(os.path.join(
            configs['templates_path'], 'data/data_detail.html'), data=data)

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
