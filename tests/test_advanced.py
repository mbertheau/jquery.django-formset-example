# -*- coding: utf-8 -*-

from .context import skeleton

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        skeleton.core.hello()


if __name__ == '__main__':
    unittest.main()
