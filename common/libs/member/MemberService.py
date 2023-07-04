import hashlib
import base64
import random
import string

import requests

from application import app, db
from common.models.member.Member import Member
from common.models.member.OauthMemberBind import OauthMemberBind
from common.libs.Helper import getCurrentDate


class MemberService:

    # 根据数据库中用户的信息生成哈希值token
    @staticmethod
    def gene_auth_code(member_info):
        m = hashlib.md5()
        raw_str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
        m.update(raw_str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def gene_salt(length=16):
        keys = [random.choice((string.ascii_letters + string.digits)) for _ in range(length)]
        return ("".join(keys))

    @staticmethod
    def getWeChatOpenId(code):
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'.format(
            app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
        res = requests.get(url).json()
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid
    
    @staticmethod
    def create_new_member(req):
        openid = req['openid'] if 'openid' in req else ''
        name = req['name'] if 'name' in req else ''
        sex = req['gender'] if 'gender' in req else 0
        avatar = req['avatarUrl'] if 'avatarUrl' in req else ''


        # 判断是否已经测试过，注册了直接返回一些信息
        bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()

        if not bind_info:
            # 创建新用户
            model_member = Member()
            model_member.name = name
            model_member.sex = sex
            model_member.avatar = avatar
            model_member.salt = MemberService.gene_salt()
            model_member.updated_time = model_member.created_time = getCurrentDate()
            db.session.add(model_member)
            db.session.commit()
            # 创建认证用户
            model_bind = OauthMemberBind()
            model_bind.member_id = model_member.id
            model_bind.type = 1
            model_bind.openid = openid
            model_bind.extra = ''
            model_bind.updated_time = model_bind.created_time = getCurrentDate()
            db.session.add(model_bind)
            db.session.commit()

        return model_member.id

    @staticmethod
    def get_member_token(member_id):
        member_info = Member.query.filter_by(id=member_id).first()
        token = "%s#%s" % (MemberService.gene_auth_code(member_info), member_info.id)
        return token
