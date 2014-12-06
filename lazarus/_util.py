# coding: utf-8
#
# This is the lazarus package _util module.
#
import os
import sys
import threading
import contextlib
import concurrent.futures as futures
from functools import partial
SingleExec = partial(futures.ThreadPoolExecutor, max_workers=1)


def defer(callable):
    '''Defers execution of the callable to a thread.

    For example:

        >>> def foo():
        ...     print('bar')
        >>> join = defer(foo)
        >>> join()
    '''
    t = threading.Thread(target=callable)
    t.start()
    return t.join


@contextlib.contextmanager
def ignored(*exceptions):
    '''Ignores any of the supplied *exceptions* during execution.

    For example, instead of:

        >>> try:
        ...     os.remove('this_file_does_not_exist')
        ... except OSError:
        ...     pass

    One could write:

        >>> with ignored(OSError):
        ...     os.remove('this_file_does_not_exist')
    '''
    try:
        yield
    except exceptions:
        pass


def close_fds():
    '''Closes open file descriptors other than stdin, stdout, and stderr.

    .. note::

        On Mac, /dev/fd/3 is a private, per-process filesystem namespace
        representing the already opened descriptor for a script interpreter.

        See http://www.sysnet.ucsd.edu/sysnet/miscpapers/tsyrklevich.pdf
        and http://perldoc.perl.org/perlsec.html
    '''
    if sys.platform == 'linux':
        fd_dir = '/proc/self/fd'
        fds = set(map(int, os.listdir(fd_dir)))
        for x in (fds - {0, 1, 2}):
            with ignored(OSError):
                os.close(x)
    elif sys.platform == 'darwin':
        fd_dir = '/dev/fd'
        fds = set(map(int, os.listdir(fd_dir)))
        for x in (fds - {0, 1, 2, 3}):
            print(x)
            with ignored(OSError):
                print(os.fstat(x))
            with ignored(OSError):
                os.close(x)


def do_over():
    '''Calls :py:func:`os.exec` with executable and args derived from sys.'''
    path = sys.executable
    args = [path] + sys.argv

    # And the rest, after a sudden wet thud, was silence.
    os.execv(path, args)
