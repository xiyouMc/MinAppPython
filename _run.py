# coding:utf-8
import requests
import re
import json
import random
import time
import string

content = [
    '感觉还是不错的……', '界面设计得不错哦！', '简约大气，素材棒棒啊。', '我不挑剔，能用就行，好评吧', '总体不错，功能强大！',
    '棒！棒！棒！', '挺好的小程序，非常喜欢', '挺好的 分享给朋友了', '体验不错，但是希望能够优化得更好', '哈哈，我觉得不错',
    '感觉这个做的挺专业', '推荐给大家用，个人觉得不错，希望能够不断改进', '整体来说很实用', '赐予五星好评奖励一下吧',
    '挺好的小程序，非常喜欢', '很简单，很方便！', '莫名的就给你一个好评，么么哒'
]

content_LJ = [
    '垃圾asdf，鉴定zdf完毕', '垃圾，鉴定fsdf完毕！', '垃圾，鉴定fsdg完毕。', '垃圾，鉴定ag完毕', '垃圾，鉴a定g完毕！',
    '棒！zsdfg棒！棒！', '垃圾z，鉴定gs完毕', '垃g圾，鉴定a完毕', '垃gsdg圾aaa，鉴定fsdf完毕', '垃圾a，鉴定b完毕',
    '垃q圾，鉴定z完毕', '垃圾g，鉴定sg完毕', '垃fasdf圾，鉴df定fsd完毕', '垃a圾，鉴b定c完毕',
    '垃z圾，鉴定f完毕', '垃f圾，鉴定e完毕', '垃a圾，鉴定g完毕'
]



def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


class MinApp(object):
    def __init__(self):
        self.r = requests.session()

    def register(self, email, username):
        default = 'https://sso.ifanr.com/embed/login/'
        f_result = self.r.get(default, verify=False)
        csrfmiddlewaretoken = re.findall(
            "name='csrfmiddlewaretoken' value='(.*?)'", f_result.text)
        print csrfmiddlewaretoken[0]
        api = 'https://sso.ifanr.com/embed/login/'
        data = {
            'csrfmiddlewaretoken': csrfmiddlewaretoken[0],
            'email': email,
            'password1': 'cxdcxd',
            'password2': 'cxdcxd',
            'nick_name': username
        }
        headers = {
            'origin':
            'https://sso.ifanr.com',
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 content-type: application/x-www-form-urlencoded',
            'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'upgrade-insecure-requests':
            '1',
            'referer':
            'https://sso.ifanr.com/embed/login/'
        }
        result = self.r.post(api, data=data, verify=False, headers=headers)
        print len(result.history)
        print result.status_code
        # Login
        self.r = None
        self.r = requests.session()
        default = 'https://sso.ifanr.com/embed/login/'
        f_result = self.r.get(default, verify=False)
        csrfmiddlewaretoken = re.findall(
            "name='csrfmiddlewaretoken' value='(.*?)'", f_result.text)
        print csrfmiddlewaretoken[0]
        loginApi = 'https://sso.ifanr.com/embed/login/?referer=http://www.ifanr.com/'
        data = {
            'csrfmiddlewaretoken': csrfmiddlewaretoken[0],
            'username': email,
            'password': 'cxdcxd'
        }
        headers = {
            'origin':
            'https://sso.ifanr.com',
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 content-type: application/x-www-form-urlencoded',
            'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'upgrade-insecure-requests':
            '1',
            'referer':
            'https://sso.ifanr.com/embed/login/?referer=http://www.ifanr.com/'
        }
        time.sleep(2)

        login = self.r.post(loginApi, data=data, verify=False, headers=headers)
        print 'login->>>>>>>>>>>>:', login.status_code
        if len(login.history) == 1:
            self.cookies = login.history[0].cookies
            print self.cookies

    def vote_github(self):

        api = 'https://minapp.com/api/v3/trochili/miniapp/3610/vote/'
        coo = ''
        csrftoken = ''
        for c in self.cookies:
            print c.name, c.value
            if c.name is 'csrftoken':
                csrftoken = c.value
                print c.value
            if c.name is 'Cookie':
                pass
            else:
                print c
                if coo is not '':
                    coo = coo + ';' + c.name + '=' + c.value
                else:
                    coo = c.name + '=' + c.value
        print "self.cookies['csrftoken']:", self.cookies['csrftoken']
        headers = {
            'Cookie':
            coo,
            'Origin':
            'https://minapp.com',
            'X-CSRFToken':
            self.cookies['csrftoken'],
            'Referer':
            'https://minapp.com/miniapp/3610/',
            'Accept':
            'application/json, text/plain, */*',
            'Accept-Encoding':
            'gzip, deflate, br',
            'Accept-Language':
            'zh-CN,zh;q=0.8,en;q=0.6',
            'Content-Type':
            'application/json;charset=UTF-8',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }

        data = {}
        result = self.r.post(
            api, data=json.dumps(data), headers=headers, verify=False)
        print result.status_code

    def rate_min(self):
        # https://minapp.com/miniapp/3640/
        # https://minapp.com/api/v3/trochili/miniapp/3640/rate/
        # https://minapp.com/miniapp/263/
        api = 'https://minapp.com/api/v3/trochili/miniapp/263/rate/'
        data = {
            'content': content_LJ[random.randint(0, len(content) - 1)],
            'score': 1
        }
        coo = ''
        csrftoken = ''
        for c in self.cookies:
            print c.name, c.value
            if c.name is 'csrftoken':
                csrftoken = c.value
                print c.value
            if c.name is 'Cookie':
                pass
            else:
                print c
                if coo is not '':
                    coo = coo + ';' + c.name + '=' + c.value
                else:
                    coo = c.name + '=' + c.value
        print "self.cookies['csrftoken']:", self.cookies['csrftoken']
        headers = {
            'Cookie':
            coo,
            'Origin':
            'https://minapp.com',
            'X-CSRFToken':
            self.cookies['csrftoken'],
            'Referer':
            'https://minapp.com/miniapp/263/',
            'Accept':
            'application/json, text/plain, */*',
            'Accept-Encoding':
            'gzip, deflate, br',
            'Accept-Language':
            'zh-CN,zh;q=0.8,en;q=0.6',
            'Content-Type':
            'application/json;charset=UTF-8',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        result = self.r.post(
            api, data=json.dumps(data), headers=headers, verify=False)
        print 'Rate:', result.status_code


if __name__ == '__main__':
    for i in range(10000):
        m = MinApp()
        m.register(
            str(random.randint(0, 10)) + 'xi90118@' +
            str(random.randint(0, 140)) + 'gmail.com',
            random_char(5) + str(random.randint(0, 10000)))
        # m.vote_github()
        m.rate_min()
        if m is not None:
            m = None
            time.sleep(3)