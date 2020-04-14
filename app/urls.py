# _*_ coding: utf-8 _*_
from app.admin.view_admin_index import IndexHandler as admin_index
from app.api.view_index import IndexHandler as api_index
from app.userInfo.view_account import AccountAddHandler as user_add_account, LoginHandler as login_index
from app.data.view_data import DataHandler as data_index, DataUploadHandler as data_upload_index, DataDetail as detail_data_index
from app.models.view_model import ModelHandler as models_index, AddModelHandler as add_model_index, ModelDetail as detail_model_index
from app.machine.view_machine import MachineHandler as machine_index, AddMachineHandler as add_machine_index, MachineDetail as detail_machine_index

from app.api.upload import FileUploadHandler as nginx_file_upload_bak_index
from app.api.jupyter import JupyterHandler as jupyter_index
from app.api.image import ImageHandler as image_index


from app.zone.view_zone_index import IndexHandler as zone_index

import tornado
from app.configs import configs
# api接口
api_urls = [
    (r'/', api_index),
    (r'/upload', nginx_file_upload_bak_index),
    (r'/jupyter', jupyter_index),
    (r'/image', image_index),
    (r'/data/', data_index),
    (r'/data/upload/', data_upload_index),
    (r'/data/detail', detail_data_index),

    (r'/models/', models_index),
    (r'/models/add/', add_model_index),
    (r'/models/detail', detail_model_index),

    (r'/machine/', machine_index),
    (r'/machine/add/', add_machine_index),
    (r'/machine/detail', detail_machine_index),
]

# 静态文件
# static_urls = [
#     (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,dict(path=configs['static_path']))
#      ]

# 后台系统
admin_urls = [
    (r'/admin', admin_index)
]


# 个人中心
zone_urls = [
    (r'/zone', zone_index)
]

# 用户登录
user_urls = [
    (r'/user/add/', user_add_account),
    (r'/user/login/', login_index),

]

urls = api_urls + admin_urls + user_urls + zone_urls

print(urls)
