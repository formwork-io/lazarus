# coding: utf-8
import os
import lazarus
import unittest
import threading


class TestLazarus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.assertFalse(lazarus._active)

    def tearDown(self):
        self.assertFalse(lazarus._active)

    def test_issue1(self):
        '''Test providing restart command (issue #1)'''
        ev = threading.Event()

        def _func():
            ev.set()

        lazarus.default(restart_func=_func, close_fds=False)
        self.assertTrue(lazarus._active)
        self.assertEquals(_func, lazarus._restart_func)
        es = os.system('touch %s' % __file__)
        self.assertEquals(0, es)

        # assert the restart function was invoked...
        self.assertTrue(ev.wait(5), 'restart function not called')

        # ... and lazarus has stopped
        self.assertEquals(False, lazarus._active)
        self.assertEquals(False, lazarus._close_fds)
        self.assertEquals(None, lazarus._restart_cb)
        self.assertEquals(None, lazarus._restart_func)

    def test_issue2(self):
        '''Test cancelling restart (issue #2)'''
        ev = threading.Event()

        def _func():
            ev.set()

        def _cb():
            return False

        lazarus.default(restart_func=_func, restart_cb=_cb, close_fds=False)
        self.assertTrue(lazarus._active)
        self.assertEquals(_func, lazarus._restart_func)
        self.assertEquals(_cb, lazarus._restart_cb)
        es = os.system('touch %s' % __file__)
        self.assertEquals(0, es)

        # assert the restart function was not invoked...
        self.assertFalse(ev.wait(5), 'restart function not called')

        # ... and lazarus has not stopped
        self.assertEquals(True, lazarus._active)
        lazarus.stop()
