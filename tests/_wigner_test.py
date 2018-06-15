import unittest, wignerpy._wignerpy as wp
import numpy as np
import os, time, math

class TestMethods(unittest.TestCase):
    #def setUp(self):
        #self.
    def test_wigner3j_smalll(self):
        correctanswer = np.fromfile(os.path.dirname(os.path.realpath(__file__)) + '/testset_smalll_128',dtype='float64').reshape(1000,7)
        #np.testing.assert_approx_equal(correctanswer[:,-1], np.array([wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]) for item in correctanswer]))
        pas = True
        for item in correctanswer:
            if abs((item[6] - wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]))/item[6]) > 1e-10:
                print(item[:6].astype('int32'), item[6], wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]))
                pas = False
        self.assertTrue(pas)

    def test_wigner3j_largel(self):
        correctanswer = np.fromfile(os.path.dirname(os.path.realpath(__file__)) + '/testset_largel_1024',dtype='float64').reshape(1000,7)
        #np.testing.assert_almost_equal(correctanswer[:,-1], np.array([wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]) for item in correctanswer]))
        pas = True
        for item in correctanswer:
            if abs((item[6] - wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]))/item[6]) > 1e-10:
                print(item[:6].astype('int32'), item[6], wp.wigner3j(item[0],item[1],item[2],item[3],item[4],item[5]))
                pas = False
        self.assertTrue(pas)
    def test_bug1(self):
        self.assertAlmostEqual(wp.test(), -0.00091099434249049543934, 15)
    def test_bug2(self):
        self.assertAlmostEqual(wp.wigner3j(529, 992, 1243, 196, -901, 705), 1.97986e-18, 23)
    def test_bug3(self):
        self.assertAlmostEqual(wp.wigner3j(751, 856, 1200, 464, -828, 364), -9.41731061215e-58, 62)
if __name__ == '__main__':
    unittest.main()
