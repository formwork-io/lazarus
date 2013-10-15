# coding: utf-8
import time
import unittest
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

        def wait1():
            time.sleep(1)

        pt = _threading.PollThread(wait1, poll_interval=0)

        # poll thread constructed as daemon
        self.assertTrue(pt.isDaemon())

        # poll thread hasn't started
        self.assertFalse(pt.isAlive())

        # start the thread
        pt.start()
        # note the current datetime t0
        t0 = datetime.now()
        # assert it's alive
        self.assertTrue(pt.isAlive())

        # change its interval to 1 seconds
        _threading.change_poll_interval(1)

        # stop the thread and join it
        pt.stop()
        pt.join()

        # note the current datetime t1
        t1 = datetime.now()

        # the time delta (t1 - t0) should be > 2 seconds
        delta = (t1 - t0).total_seconds()
        # (sleep in the poll function plus the interval)
        self.assertGreater(delta, 2, 'the delta was too small (%s)' % delta)

        # assert it is dead
        self.assertFalse(pt.isAlive())
