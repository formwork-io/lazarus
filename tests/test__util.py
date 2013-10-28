# coding: utf-8
import os
import lazarus
import unittest


class TestUtilFuncs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ignored(self):
        with lazarus._util.ignored(OSError):
            self.assertTrue(True)
        global called
        called = False
        with lazarus._util.ignored(OSError):
            os.remove('this_does_not_exist')
            called = True
        self.assertFalse(called)

    def test_close_fds(self):
        global called
        called = False

        def _close(x):
            global called
            called = True

        close = os.close
        os.close = _close
        lazarus._util.close_fds()
        self.assertTrue(called)
        os.close = close

    def test_do_over(self):
        global called
        called = False
        execv = os.execv

        def _execv(*args):
            global called
            called = True

        os.execv = _execv
        lazarus._util.do_over()
        self.assertTrue(called)
        os.execv = execv
