# coding=utf-8

import requests
import unittest


class TestWorkWeixin(unittest.TestCase):
    def setUp(self):
        """
        获取access_token
        请求方式： GET（HTTPS）
        请求地址： https: // qyapi.weixin.qq.com / cgi - bin / gettoken?corpid = ID & corpsecret = SECRET
        """
        corpid = "ww4d0bba9471093997"
        Secret = "0MigdQU7pzCVLHwF2h55Ttxsr9EG8T6oMaREdu4o5SM"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={Secret}"
        data = requests.get(url).json()
        self.access_token = data["access_token"]

    def test_get_api(self):
        """
        获取企业微信API域名IP段
        请求方式：GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=ACCESS_TOKEN （获取ACCESS_TOKEN）
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token={self.access_token}"
        data = requests.get(url).json()
        print(data)


    def test_create_user(self):
        """
        创建成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        data = {
                "userid": "xiaob123",  # 成员UserID。对应管理端的帐号，企业内必须唯一。
                "name": str("按顺序".encode("utf-8")),  # 成员名称。长度为1~64个utf8字符
                "mobile": 13026123400,  # 手机号码。企业内必须唯一，mobile / email二者不能同时为空
                "department": 2,  # 成员所属部门id列表，不超过100个
            }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}&debug=1"
        data = requests.post(url, json=data).json()
        print(data)

    def test_get_user(self):
        """
        读取成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        userid = 'xiaob123'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={userid}"
        data = requests.get(url).json()
        print(data)


    def test_update_user(self):
        """
        更新成员
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        data = {
                "userid": "xiaob123",  # 成员UserID。对应管理端的帐号，企业内必须唯一。
                "name": "123456789465",  # 成员名称。长度为1~64个utf8字符
                "department": 3,  # 成员所属部门id列表，不超过100个
            }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}"
        data = requests.post(url, json=data).json()
        print(data)


    def test_message_send(self):
        """
        发送应用消息
        应用支持推送文本、图片、视频、文件、图文等类型。
        请求方式：POST（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN
        """
        data = {
                   "toparty" : 2,
                   # "toparty" : "PartyID1|PartyID2",
                   # "totag" : "TagID1 | TagID2",
                   "msgtype" : "text",
                   "agentid" : 1000002,
                   "text" : {
                       "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
                   },
                   # "safe":0,
                   # "enable_id_trans": 0,
                   # "enable_duplicate_check": 0,
                   # "duplicate_check_interval": 1800
                }

        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.access_token}"
        data = requests.post(url, json=data).json()
        print(data)
