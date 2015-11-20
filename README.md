#都散了，别用了。


acfun-api-replace-server
==============

Replacing API server of Acfun to retrive original source from ```letvcloud``` instead of the shitty one.

You can use https://acfunfix.sinaapp.com/?vid=   , but I do not want to replace the original player for some good reasons.

Sample Public API avalable at https://acfun-api.cnbeining.com/getVideo?id=  , Cloudflare + Openshift, so do not expect much speed.

How to use this?
--------------------
Check https://www.cnbeining.com/?p=1014  .


Why so much hate?
--------------------

https://gist.github.com/cnbeining/ec8c74df1934a943bcf9

Sample outcome
--------------------

```

$curl http://www.acfun.tv/video/getVideo.aspx?id=2318907

{"sourceId":"b4bb55f7ff","contentId":1980501,"allowDanmaku":0,"title":"Part 1","userId":382427,"danmakuId":2318907,"sourceUrl":"b4bb55f7ff","sourceType":"zhuzhan","createTime":"2015-06-24 03:13:58.0","videoList":[{"bitRate":1,"playUrl":"http://vplay.aixifan.com/des/acf-47/2318907_mp4/2318907_360p.mp4?k=6766de4527a96a6dfbad6cb28bfb4304&t=1446572031"},{"bitRate":2,"playUrl":"http://vplay.aixifan.com/des/acf-47/2318907_mp4/2318907_480p.mp4?k=64560667bd1c1d388bf1930d46b3314f&t=1446572031"},{"bitRate":3,"playUrl":"http://vplay.aixifan.com/des/acf-47/2318907_mp4/2318907_720p.mp4?k=55c995fd7f308f786492b8586cb0b257&t=1446572031"}],"success":true,"startTime":0,"id":2318907,"time":184,"config":0,"status":2}

$curl https://acfun-api.cnbeining.com/getVideo?id=2318907

{"status": 2, "sourceUrl": "b4bb55f7ff", "sourceType": "letv", "success": true, "title": "Part 1", "sourceId": "b4bb55f7ff", "contentId": 1980501, "userId": 382427, "startTime": 0, "createTime": "2015-06-24 03:13:58.0", "allowDanmak": 0, "time": 184, "id": 2318907, "config": 0, "danmakuId": 2318907}

```

Running on OpenShift
--------------------

Plug and run on Openshift.

Requirement
-------

- Python 2.7
- web.py
- requests

Author
-----
Beining, https://www.cnbeining.com/ , i#cnbeining.com

License
-----

GPLv2 license.

This program is provided **as is**, with absolutely no warranty.
