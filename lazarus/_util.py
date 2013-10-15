# coding: utf-8
#
# This is the lazarus package _util module.
#
import os
import sys
import contextlib
_fd_dir = '/proc/self/fd'


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
    '''Closes open file descriptors other than stdin, stdout, and stderr.'''
    if not os.path.exists(_fd_dir):
        return
    fds = set(map(int, os.listdir(_fd_dir)))
    for x in (fds - {0, 1, 2}):
        with ignored(OSError):
            os.close(x)


def do_over():
    '''Calls :py:func:`os.exec` with executable and args derived from sys.'''
    path = sys.executable
    args = [path] + sys.argv

    # And the rest, after a sudden wet thud, was silence.
    os.execv(path, args)
