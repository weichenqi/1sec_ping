#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2017-08-09 09:00 
# @Author  : George Wei (weichenqi@gmail.com)
# @Link    : http://weichenqi.com
# @Version : 0.1

import pyping, datetime
print datetime.datetime.now()
for iplist in range(1, 255):
    r = pyping.ping('192.168.1.'+str(iplist), count=1, packet_size=1, timeout=2, udp=True) #默认icmp ping，根据实际情况开启udp ping
    print "192.168.1."+str(iplist) +" status:" + str(r.ret_code)
print datetime.datetime.now()
