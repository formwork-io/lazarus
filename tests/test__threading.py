# coding: utf-8
import time
import unittest
import threading
from datetime import datetime
from lazarus import _threading


class TestPollThread(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_init(self):
        '''Test creating a PollThread'''

        def function():
            pass

        pt = _threading.PollThread(function)

        # poll thread constructed as daemon
        self.assertTrue(pt.isDaemon())

        # poll thread hasn't started
        self.assertFalse(pt.isAlive())

    def test_join(self):
        '''Test joining a PollThread'''

        def function():
            pass

        pt = _threading.PollThread(function, poll_interval=0.25)

        # poll thread constructed as daemon
        self.assertTrue(pt.isDaemon())

        # poll thread hasn't started
        self.assertFalse(pt.isAlive())

        # start the thread
        pt.start()
        # assert it's alive
        self.assertTrue(pt.isAlive())

        # stop the thread and join it
        pt.stop()
        pt.join()

        # assert it is dead
        self.assertFalse(pt.isAlive())

    def test_change_interval(self):
        '''Test changing a PollThread interval'''

        step1 = threading.Event()
        step2 = threading.Event()

        def wait1():
            step1.set()
            if not step2.wait(5):
                self.fail('timeout: failed waiting for sync point')
            step2.clear()

        pt = _threading.PollThread(wait1, poll_interval=0.01)

        # poll thread constructed as daemon
        self.assertTrue(pt.isDaemon())

        # poll thread hasn't started
        self.assertFalse(pt.isAlive())

        # start the thread
        pt.start()
        # assert it's alive
        self.assertTrue(pt.isAlive())

        # wait until thread arrives
        if not step1.wait(5):
            self.fail('timeout: failed waiting for sync point')
        # reset while thread waits
        step1.clear()

        # change its interval to 0.25 seconds
        _threading.change_poll_interval(0.25)

        # note the current datetime t0
        t0 = datetime.now()

        # let thread continue
        step2.set()
        # wait until thread arrives
        if not step1.wait(5):
            self.fail('timeout: failed waiting for sync point')
        # reset while thread waits (not necessary)
        step1.clear()

        # note the current datetime t0
        t1 = datetime.now()

        # stop the thread and join it
        pt.stop()
        step2.set()
        pt.join()

        # the time delta (t1 - t0) should be > 2 seconds
        delta = (t1 - t0).total_seconds()
        # (sleep in the poll function plus the interval)
        self.assertGreater(delta, 0.25, 'the delta was too small (%s)' % delta)

        # assert it is dead
        self.assertFalse(pt.isAlive())
