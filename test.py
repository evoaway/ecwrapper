import random
import unittest
from ecwrapper import *
from fastecdsa.curve import P192

class TestStringMethods(unittest.TestCase):
    def test_equation(self):
        curve = Curve()
        G = curve.BasePointGGet()
        k = random.getrandbits(256)
        d = random.getrandbits(256)

        H1 = ScalarMult(d, G)
        H2 = ScalarMult(k, H1)

        H3 = ScalarMult(k, G)
        H4 = ScalarMult(d, H3)

        self.assertEqual(H2, H4)

    def test_operations(self):
        xs = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
        ys = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256
        S = ECPoint(xs, ys)

        xt = 0x55a8b00f8da1d44e62f6b3b25316212e39540dc861c89575bb8cf92e35e0986b
        yt = 0x5421c3209c2d6c704835d82ac4c3dd90f61a8a52598b9e7ab656e9d8c8b24316
        T = ECPointGen(xt, yt)

        R = AddECPoints(S, T)
        self.assertEqual(R, ECPoint(0x72b13dd4354b6b81745195e98cc5ba6970349191ac476bd4553cf35a545a067e,
                                    0x8d585cbb2e1327d75241a8a122d7620dc33b13315aa5c9d46d013011744ac264))

        R = DoubleECPoints(S)
        self.assertEqual(R, ECPoint(0x7669e6901606ee3ba1a8eef1e0024c33df6c22f3b17481b82a860ffcdb6127b0,
                                    0xfa878162187a54f6c39f6ee0072f33de389ef3eecd03023de10ca2c1db61d0c7))

    def test_curve(self):
        curve = Curve()
        xs = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
        ys = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256
        S = ECPoint(xs, ys)
        self.assertTrue(curve.IsOnCurveCheck(S))

        curve192 = Curve(P192)
        self.assertFalse(curve192.IsOnCurveCheck(S))

    def test_string(self):
        xs = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
        ys = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256
        S = ECPoint(xs, ys)
        PrintECPoint(S)

        str_p = ECPointToString(S)
        S1 = StringToECPoint(str_p)
        PrintECPoint(S1)

        self.assertEqual(S, S1)


if __name__ == '__main__':
    unittest.main()
