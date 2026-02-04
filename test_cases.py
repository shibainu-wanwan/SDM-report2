#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        def test_valid_boundary(self):
            # 最小値の境界 (1, 1) -> 1
            self.assertEqual(1, calc(1, 1))
            # 最大値の境界 (999, 999) -> 998001
            self.assertEqual(998001, calc(999, 999))

        def test_invalid_boundary_low(self):
            # 0は範囲外なので -1 を返すべき
            self.assertEqual(-1, calc(0, 500))
            self.assertEqual(-1, calc(500, 0))

        def test_invalid_boundary_high(self):
            # 1000は範囲外なので -1 を返すべき
            self.assertEqual(-1, calc(1000, 500))
            self.assertEqual(-1, calc(500, 1000))

        def test_invalid_type(self):
            # 小数や文字列は -1 を返すべき
            self.assertEqual(-1, calc(0.1, 999))
            self.assertEqual(-1, calc("a", 999))
