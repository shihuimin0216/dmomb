class Model:
    def __init__(self, uuid, name, paper, data_url, file_path, jupyter_path, img_path, info, createAt, updatedAt):
        self.uuid = uuid
        self.name = name
        self.paper = paper
        self.data_url = data_url
        self.file_path = file_path
        self.jupyter_path = jupyter_path
        self.img_path = img_path
        self.info = info
        self.createAt = createAt
        self.updatedAt = updatedAt

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ('uuid', 'name', 'paper', 'data_url', 'file_path',
                'jupyter_path', 'img_path', 'info', 'createAt', 'updatedAt')

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

    # @property
    # def m_id(self):
    #     return self.m_id

    # @m_id.setter
    # def m_id(self, m_id):
    #     self.m_id = m_id

    # @property
    # def name(self):
    #     return self.name

    # @name.setter
    # def name(self, name):
    #     self.name = name

    # @property
    # def paper(self):
    #     return self.paper

    # @paper.setter
    # def paper(self, paper):
    #     self.paper = paper

    # @property
    # def file_path(self):
    #     return self.file_path

    # @file_path.setter
    # def file_path(self, file_path):
    #     self.file_path = file_path

    # @property
    # def info(self):
    #     return self.info

    # @info.setter
    # def info(self, info):
    #     self.info = info

    # @property
    # def createAt(self):
    #     return self.createAt

    # @createAt.setter
    # def createAt(self, createAt):
    #     self.createAt = createAt

    # @property
    # def updatedAt(self):
    #     return self.updatedAt

    # @updatedAt.setter
    # def updatedAt(self, updatedAt):
    #     self.updatedAt = updatedAt
