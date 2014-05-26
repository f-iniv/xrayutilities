import xrayutilities as xu
import numpy
import unittest

class TestQ2Ang_nonCOP(unittest.TestCase):

    def setUp(self):
        self.mat = xu.materials.Al2O3
        self.hxrd = xu.NonCOP(self.mat.Q(1,1,0),self.mat.Q(0,0,1))
        self.hkltest = (1,2,3)
        self.hkltest2 = (-1.5,3.1,3)

    def test_Q2Ang_nonCOP_point(self):
        ang = self.hxrd.Q2Ang(self.mat.Q(self.hkltest))
        qout = self.hxrd.Ang2HKL(*ang,mat=self.mat)
        for i in range(3):
            self.assertAlmostEqual(qout[i], self.hkltest[i], places=10)

    def test_Q2Ang_nonCOP_point2(self):
        ang = self.hxrd.Q2Ang(self.mat.Q(self.hkltest2))
        qout = self.hxrd.Ang2HKL(*ang,mat=self.mat)
        for i in range(3):
            self.assertAlmostEqual(qout[i], self.hkltest2[i], places=10)
    
if __name__ == '__main__':
        unittest.main()
