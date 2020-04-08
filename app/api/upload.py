# _*_ coding: utf-8 _*_
# _*_ coding:utf-8 _*_
import tornado.gen
import tornado.concurrent
from app.api.view_common import CommonHandler


class FileUploadHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        print("upload进入get函数")
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        file_name = self.get_argument("file_name")
        print(file)
        tmp_path = self.get_argument("tmp_path")
        # do_some_thing(tmp_path)
        self.finish("file uploaded!")
        # self.write("okokok")

    def post(self, *args, **kwargs):
        # print("upload进入post函数")
        # yield self.post_response()
        # file_name = self.get_argument("name")
        # argument = self.get
        # tmp_path = self.get_argument("tmp_path")
        # print(tmp_path)
        # do_some_thing(tmp_path)
        form = self.form_params
        print(form)
        self.write({'success': 'success'})

    @tornado.concurrent.run_on_executor
    def post_response(self):
        file_name = self.get_argument("file_name")
        argument = self.get
        tmp_path = self.get_argument("tmp_path")
        print(tmp_path)
        do_some_thing(tmp_path)
        self.finish("file uploaded!")

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True
