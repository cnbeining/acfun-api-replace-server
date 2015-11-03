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
```$ mediainfo 1764019_720p.mp4
General
Complete name                            : 1764019_720p.mp4
Format                                   : MPEG-4
Format profile                           : Base Media
Codec ID                                 : isom
File size                                : 19.3 MiB
Duration                                 : 3mn 47s
Overall bit rate                         : 713 Kbps<-------WTF????
Encoded date                             : UTC 1904-01-01 00:00:00
Tagged date                              : UTC 1904-01-01 00:00:00
Writing application                      : Lavf56.15.102

Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L3.1
Format settings, CABAC                   : Yes
Format settings, ReFrames                : 4 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3mn 47s
Bit rate                                 : 658 Kbps
Nominal bit rate                         : 700 Kbpss<-------dude WTF?
Width                                    : 1 280 pixels
Height                                   : 720 pixelss<-------the original one was 1080p
Display aspect ratio                     : 16:9
Frame rate mode                          : Constants<-------seriously?????/
Frame rate                               : 25.000 fps
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.029
Stream size                              : 17.8 MiB (92%)
Writing library                          : x264 core 142 r62 24e4fed
Encoding settings                        : cabac=1 / ref=2 / deblock=1:0:0 / analyse=0x3:0x113 / me=hex / subme=6 / psy=1 / psy_rd=1.00:0.00 / mixed_ref=1 / me_range=16 / chroma_me=1 / trellis=1 / 8x8dct=1 / cqm=0 / deadzone=21,11 / fast_pskip=1 / chroma_qp_offset=-2 / threads=36 / lookahead_threads=5 / sliced_threads=0 / nr=0 / decimate=1 / interlaced=0 / bluray_compat=0 / constrained_intra=0 / bframes=3 / b_pyramid=2 / b_adapt=1 / b_bias=0 / direct=1 / weightb=1 / open_gop=0 / weightp=1 / keyint=250 / keyint_min=25 / scenecut=40 / intra_refresh=0 / rc_lookahead=30 / rc=abr / mbtree=1 / bitrate=700 / ratetol=1.0 / qcomp=0.60 / qpmin=0 / qpmax=69 / qpstep=4 / ip_ratio=1.40 / aq=1:1.00
Encoded date                             : UTC 1904-01-01 00:00:00
Tagged date                              : UTC 1904-01-01 00:00:00

Audio
ID                                       : 2
Format                                   : AAC
Format/Info                              : Advanced Audio Codec
Format profile                           : LC
Codec ID                                 : 40
Duration                                 : 3mn 47s
Duration_LastFrame                       : -10ms
Bit rate mode                            : Constant
Bit rate                                 : 48.0 Kbpss<-------WTF is this????
Channel(s)                               : 2 channels
Channel positions                        : Front: L R
Sampling rate                            : 44.1 KHz
Compression mode                         : Lossy
Stream size                              : 1.30 MiB (7%)
Encoded date                             : UTC 1904-01-01 00:00:00
Tagged date                              : UTC 1904-01-01 00:00:00
```

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
