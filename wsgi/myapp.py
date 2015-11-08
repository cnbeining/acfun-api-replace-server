#!/usr/bin/env python
#coding:utf-8
# Author:  Beining --<i#cnbeining.com>
# Purpose: Replacement of Acfun's API
# Created: 11/03/2015

import web
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

urls = (
    '/getVideo', 'getVideo',
    '/crossdomain.xml', 'crossdomain',
)

class getVideo:
    #----------------------------------------------------------------------
    def letvcloud_exist(self, vu):
        """"""
        headers = {
            'dnt': '1',
            'accept-encoding': 'gzip, deflate, sdch',
            'x-requested-with': 'ShockwaveFlash/19.0.0.226',
            'accept-language': 'en-CA,en;q=0.8,en-US;q=0.6,zh-CN;q=0.4,zh;q=0.2',
            'user-agent': '(Python-urllib/{2.7}, like libcurl/1.0 NSS-Mozilla/2.0)',
            'accept': '*/*',
        }
        api_url = 'http://api.letvcloud.com/gpc.php?&sign=signxxxxx&cf=html5&vu={vu}&ver=2.2&ran=0.6220391783863306&qr=2&format=json&uu=2d8c027396'.format(vu = vu)
        try:
            res = requests.get(api_url, headers=headers)
            res = res.json()
        except Exception as e:
            return - 1
        if not res['code'] == 0:
            return -10000
    
    def GET(self):
        user_data = web.input()
        try:  #anti BS
            id = int(user_data.id)
        except ValueError, AttributeError:
            return 'ERROR'
        
        api_url = 'http://www.acfun.tv/video/getVideo.aspx?id={id}'.format(id = id)
        
        headers = {
            'dnt': '1',
            'accept-encoding': 'gzip, deflate, sdch',
            'x-requested-with': 'ShockwaveFlash/19.0.0.226',
            'accept-language': 'en-CA,en;q=0.8,en-US;q=0.6,zh-CN;q=0.4,zh;q=0.2',
            'user-agent': 'Acfun-API / 0.0.1 (i@cnbeining.com) (Python-urllib/{2.7}, like libcurl/1.0 NSS-Mozilla/2.0)',
            'accept': '*/*',
        }        
        api_url = 'http://www.acfun.tv/video/getVideo.aspx?id={id}'.format(id = id)
        
        try:
            res = requests.get(api_url, headers=headers)
            res = res.json()
        except Exception as e:
            return 'ERROR'
        
        if not res['success']:  #failed
            return res.replace("u'", "'").replace("'", '"').replace('True', 'true')  #throw the shit back
        
        if str(res['sourceType']) == 'zhuzhan':  #compressed shit
            if self.letvcloud_exist(res['sourceUrl']) < 0:  #unrecoverable shit
                return str(res).replace("u'", "'").replace("'", '"').replace('True', 'true')
            else:
                del(res['videoList'])  #strip this
                res['sourceType'] = 'letv'  #force change back
            
        return str(res).replace("u'", "'").replace("'", '"').replace('True', 'true')

class crossdomain:
    def GET(self): 
        raise web.seeother("/static/crossdomain.xml")

app = web.application(urls, globals())
#app.run()
application = app.wsgifunc()
