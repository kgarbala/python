# Krzysztof Garbala
# -*- coding: utf-8 -*-

import time, iteratory
tick=time.time()
localtime = time.localtime(time.time())
print "Local current time :", localtime

localtime = time.asctime(time.localtime(time.time()) )
print "Local current time :", localtime
print 	time.clock( )
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print "returned tuple: %s " % struct_time