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
    '/getVideo', 'getVideo'
)

class getVideo:
    def GET(self):
        user_data = web.input()
        try:  #anti BS
            id = int(user_data.id)
        except ValueError, AttributeError:
            return 'ERROR'
        
        api_url = 'http://www.acfun.tv/video/getVideo.aspx?id={id}'.format(id = id)
        
        try:
            res = requests.get(api_url)
            res = res.json()
        except Exception as e:
            return 'ERROR'
        
        if not res['success']:  #failed
            return res.replace("u'", "'").replace("'", '"').replace('True', 'true')  #throw the shit back
        
        if str(res['sourceType']) == 'zhuzhan':  #compressed shit
            del(res['videoList'])  #strip this
            res['sourceType'] = 'letv'  #force change back
            
        return str(res).replace("u'", "'").replace("'", '"').replace('True', 'true')

app = web.application(urls, globals())
#app.run()
application = app.wsgifunc()
