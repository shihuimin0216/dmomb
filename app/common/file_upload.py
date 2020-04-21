# _*_ coding: utf-8 _*_
import os
import uuid
from app.api.html_common import HtmlHandler
from app.common.jupyter_to_html import Jupyter_to_html as jh


class FileUpload(HtmlHandler):
    def __init__(self, file_metas):
        self.file_metas = file_metas

    @property
    def save_file(self):
        if self.file_metas is not None:
            for meta in self.file_metas:
                filename = meta['filename']
                # file_uuid = uuid.uuid4()
                file_path = os.path.join(self.upload_path, filename)
                print(file_path)
                self.file_db = os.path.join(self.file_db_path, filename)
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
            return True
        else:
            return False

    @property
    def save_to_html(self):
        if self.file_metas is not None:
            for meta in self.file_metas:
                # filename = meta['filename']
                # 重新定义一个独一无二的名字
                file_uuid = str(uuid.uuid4())
                filename = file_uuid + '.html'
                # jupyter转换成html
                html = jh.to_html(meta['body'])
                # print(html)
                file_path = os.path.join(self.upload_path, filename)
                print(file_path)
                self.file_db = os.path.join(self.file_db_path, filename)
                with open(file_path, 'w') as up:
                    up.write(html)
            return True
        else:
            return False
