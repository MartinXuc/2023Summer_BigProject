import os
import stat
import uuid

from werkzeug.utils import secure_filename

from common.models.db import db

from common.config.base_setting import UPLOAD, APP
from common.libs.Helper import getCurrentDate
from common.models.Image import Image


class UploadService():
    @staticmethod
    def upload_by_file(file):
        resp = {'code': 200, 'msg': 'success', 'data': {}}
        filename = secure_filename(file.filename)
        ext = filename.rsplit('.', 1)[1]
        if ext not in UPLOAD['ext']:
            resp['code'] = -1
            resp['msg'] = '不允许的扩展类型文件！'

        root_path = APP['root_path'] + UPLOAD['prefix_path']
        file_dir = getCurrentDate('%Y%m%d')
        save_dir = root_path + file_dir
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
            os.chmod(save_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)

        file_name = str(uuid.uuid4()).replace('-', '') + '.' + ext
        file.save('{0}/{1}'.format(save_dir, file_name))

        model_iamge = Image()
        model_iamge.file_key = file_dir + '/' + file_name
        model_iamge.created_time = getCurrentDate()
        db.session.add(model_iamge)
        db.session.commit()

        resp['data'] = {
            'file_key': file_dir + '/' + file_name
        }

        return resp
