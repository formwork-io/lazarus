# coding: utf-8
import os
import time
import lazarus
import unittest


class TestLazarus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_issue1(self):
        '''Test providing restart command (issue #1)'''
        self.assertFalse(lazarus._active)
        self.called = False

        def _func():
            self.called = True

        lazarus.default(restart_func=_func, close_fds=False)
        self.assertTrue(lazarus._active)
        self.assertEquals(_func, lazarus._restart_func)
        os.system('touch %s' % __file__)
        time.sleep(1.25)

        # assert the restart function was invoked...
        self.assertTrue(self.called)

        # ... and lazarus has stopped
        self.assertEquals(False, lazarus._active)
        self.assertEquals(False, lazarus._close_fds)
        self.assertEquals(None, lazarus._restart_cb)
        self.assertEquals(None, lazarus._restart_func)
        self.assertEquals(None, lazarus._pollthread)
        self.assertEquals(None, lazarus._mgr)
        self.assertEquals(None, lazarus._notifier)

    def test_issue2(self):
        '''Test cancelling restart (issue #2)'''
        self.assertFalse(lazarus._active)
        self.called = False

        def _func():
            self.called = True

        def _cb():
            return False

        lazarus.default(restart_func=_func, restart_cb=_cb, close_fds=False)
        self.assertTrue(lazarus._active)
        self.assertEquals(_func, lazarus._restart_func)
        self.assertEquals(_cb, lazarus._restart_cb)
        os.system('touch %s' % __file__)
        time.sleep(1.25)

        # assert the restart function was not invoked...
        self.assertFalse(self.called)

        # ... and lazarus has not stopped
        self.assertEquals(True, lazarus._active)
