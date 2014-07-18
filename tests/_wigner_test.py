import unittest, wignerpy._wignerpy as wp
import numpy as np
import commands, os, time, math

class TestMethods(unittest.TestCase):
    #def setUp(self):
        #self.
    def test_wigner3j_smalll(self):
        correctanswer = np.fromfile(os.path.dirname(os.path.realpath(__file__)) + '/testset_smalll_128',dtype='float64').reshape(1000,7)
        np.testing.assert_almost_equal(correctanswer[:,-1], np.array([wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]) for item in correctanswer]))
    def test_wigner3j_largel(self):
        correctanswer = np.fromfile(os.path.dirname(os.path.realpath(__file__)) + '/testset_largel_1024',dtype='float64').reshape(1000,7)
        np.testing.assert_almost_equal(correctanswer[:,-1], np.array([wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]) for item in correctanswer]))
    def test_fixed(self):
        self.assertAlmostEqual(wp.test(), -0.00091099434249049543934, 15)
    def test_tmp_fix(self):
        self.assertAlmostEqual(wp.wigner3j(827, 1020, 1570, 590, 902, -1492), -0.00091099434249049543934, 15)
if __name__ == '__main__':
    unittest.main()