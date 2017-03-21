#
#
#
import subprocess

uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])

diskspace = "df"
disk_arg = "-h"
print "disk space is %s:\n" % diskspace
subprocess.call([diskspace, disk_arg])
