# -*- coding: utf-8 -*-

"""
Python runner for graphit module unit tests, run as:
::
    python tests
"""

import os
import sys
import unittest
import logging

# Init basic logging
logging.basicConfig(level=logging.WARN)

# Add modules in package to path so we can import them
modulepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, modulepath)


def module_test_suite():
    """
    Run graphit module unit tests.
    """
    loader = unittest.TestLoader()

    print('Running graphit unittests')
    testpath = os.path.join(os.path.dirname(__file__), 'module')
    suite = loader.discover(testpath, pattern='module_storage*.py')
    runner = unittest.TextTestRunner(verbosity=2)

    return runner.run(suite).wasSuccessful()


if __name__ == '__main__':
    ret = module_test_suite()
    sys.exit(not ret)