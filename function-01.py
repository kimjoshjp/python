#
#
#
#
#

import os
import time
import calendar

if os.path.isdir("/tmp"):
    print "/tmp is a dir"

else:
    print "/tmp is not a dir"

##

localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

##
cal = calendar.month(1970, 2)
print " Here is the calendar of 1970"
print cal
