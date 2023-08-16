import time
from common.config.base_setting import APP, UPLOAD

class UrlManager:
    def __init__(self):
        pass

    @staticmethod
    def build_url(path):
        return path

    @classmethod
    def static_url(cls, path):
        ver = "%s" % int(time.time())
        path = '/static' + path + "?ver=" + ver
        return cls.build_url(path)

    @staticmethod
    def build_image_url(path):
        
        url = APP['domain'] + UPLOAD['prefix_url'] + path
        return url

    @staticmethod
    def build_res(res):
        if res:
            for key in res:
                res[key] = UrlManager.build_image_url(res[key])
