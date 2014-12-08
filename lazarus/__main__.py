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

fd = False
compat = True

sys.stdout.write('Checking for /proc/self/fd... ')
if os.path.exists('/proc/self/fd'):
    print('yes')
    fd = True
else:
    print('no')

sys.stdout.write('Checking for /dev/fd... ')
if os.path.exists('/dev/fd'):
    print('yes')
    fd = True
else:
    print('no')

if not fd:
    compat = False

sys.stdout.write('Checking for watchdog... ')
try:
    import watchdog.observers
    print('yes')
except ImportError as ie:
    print('no (%s)' % str(ie))
    compat = False

sys.stdout.write('Checking for API compatibility... ')
try:
    watchdog.observers.Observer
    print('yes')
except AttributeError as ae:
    print('no (%s)' % str(ae))
    compat = False

if compat:
    print('All compatiblity checks passed.')
    sys.exit(0)
else:
    print('One or more compatiblity checks failed.')
    sys.exit(1)
