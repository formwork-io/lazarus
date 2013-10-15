# coding: utf-8
#
# This is the lazarus library's __main__ module.
#
import os
import sys
msg = '''\
This is the lazarus library for Python.\
'''
print(msg)

msg = '''\
Executing compatiblity check.\
'''
print(msg)

compat = True

sys.stdout.write('Checking for /proc/self/fd... ')
if os.path.exists('/proc/self/fd'):
    print('yes')
else:
    print('no')
    compat = False

sys.stdout.write('Checking for pyinotify... ')
try:
    from pyinotify import (
        ProcessEvent,
        WatchManager,
        Notifier,
        IN_MODIFY,
        IN_CLOSE_WRITE,
        IN_CREATE,
        IN_MOVED_TO
    )
    print('yes')
except ImportError as ie:
    print('no (%s)' % str(ie))
    compat = False

if compat:
    print('All compatiblity checks passed.')
    sys.exit(0)
else:
    print('One or more compatiblity checks failed.')
    sys.exit(1)
