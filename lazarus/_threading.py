# coding: utf-8
import os
import time
import threading
_mutex = threading.Lock()
_interval = 1.0


def change_poll_interval(interval):
    '''Change the poll interval.'''
    global _interval
    with _mutex:
        _interval = float(interval)


def get_poll_interval():
    '''Get the poll interval.

    The poll interval returned is not guaranteed to be the latest configured
    interval.
    '''
    return _interval


def get_poll_interval_safe():
    '''Get the latest poll interval.

    The poll interval returned is guaranteed to be the latest configured
    interval.
    '''
    with _mutex:
        return _interval


class PollThread(threading.Thread):

    def __init__(self, poll_function, poll_interval=1):
        change_poll_interval(poll_interval)
        name = 'lazarus-poll-thread-%d' % os.getpid()
        kwargs = {'target': self._target, 'name': name}
        threading.Thread.__init__(self, **kwargs)
        self.daemon = True
        self._poll_function = poll_function
        self._event = threading.Event()

    def _target(self):
        while not self._event.is_set():
            self._poll_function()
            time.sleep(get_poll_interval_safe())

    def stop(self):
        self._event.set()
