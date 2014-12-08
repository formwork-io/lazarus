# coding: utf-8
#
# This is the lazarus package _util module.
#
import os
import sys
import threading
import contextlib


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
    '''Close extraneous file descriptors.

    On Linux, close everything but stdin, stdout, and stderr. On Mac, close
    stdin, stdout, and stderr and everything owned by our user id.
    '''
    def close(fd):
        with ignored(OSError):
            os.close(fd)

    if sys.platform == 'linux':
        fd_dir = '/proc/self/fd'
        fds = set(map(int, os.listdir(fd_dir)))
        for x in (fds - {0, 1, 2}):
            close(x)

    elif sys.platform == 'darwin':
        uid = os.getuid()
        fd_dir = '/dev/fd'
        fds = set(map(int, os.listdir(fd_dir)))
        for x in (fds - {0, 1, 2}):
            path = '/dev/fd/' + str(x)
            if not os.access(path, os.R_OK):
                continue
            stat = os.fstat(x)
            if stat.st_uid != uid:
                continue
            close(x)


def do_over():
    '''Calls :py:func:`os.exec` with executable and args derived from sys.'''
    path = sys.executable
    args = [path] + sys.argv

    # And the rest, after a sudden wet thud, was silence.
    os.execv(path, args)
