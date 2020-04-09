# _*_ coding: utf-8 _*_
import tornado.gen
import tornado.concurrent
from app.api.view_common import CommonHandler
from app.common.file_upload import FileUpload

# /jupyter


class ImageHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.write("访问错误")

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        # post获取传过来的文件
        file_metas = self.request.files.get('image', None)
        # 将文件进行保存
        file_saver = FileUpload(file_metas)
        # 文件保存成功
        if file_saver.save_file:
            print(file_saver)
            res = {
                'success': 'success'
            }
            # 获取文件的路径
            file_db = file_saver.file_db
            # 将文件路径写入cookie中
            self.set_secure_cookie('image_path', file_db)
        else:
            res = {}
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True
