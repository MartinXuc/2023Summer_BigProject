import hashlib
import random
import string

import requests
from common.models.db import db
from common.config.base_setting import MINA_APP

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
        if code is None:
            return None
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'.format(
            MINA_APP['app_id'], MINA_APP['app_secret'], code)
        
        
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
        id = None
        if bind_info:
            id = bind_info.member_id

        else:
            # 创建新用户
            member = Member()
            member.name = name
            member.sex = sex
            member.avatar = avatar
            member.salt = MemberService.gene_salt()
            member.updated_time = member.created_time = getCurrentDate()
            db.session.add(member)
            db.session.commit()
            # 创建认证用户
            member_bind = OauthMemberBind()
            member_bind.member_id = member.id
            member_bind.type = 1
            member_bind.openid = openid
            member_bind.extra = ''
            member_bind.updated_time = member_bind.created_time = getCurrentDate()
            db.session.add(member_bind)
            db.session.commit()
            id = member.id

        return id

    @staticmethod
    def get_member_token(member_id):
        member_info = Member.query.filter_by(id=member_id).first()
        token = "%s#%s" % (MemberService.gene_auth_code(member_info), member_info.id)
        return token
