from fastecdsa import curve
from fastecdsa.point import Point


class ECPoint:
    def __init__(self, x: int, y: int, curve=curve.P256):
        self.x = x
        self.y = y
        self.curve = curve

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.curve == other.curve


class Curve:
    def __init__(self, curve=curve.P256):
        self.curve = curve

    def BasePointGGet(self):
        return ECPoint(self.curve.G.x, self.curve.G.y, self.curve)

    def IsOnCurveCheck(self, point: ECPoint):
        return self.curve.is_point_on_curve((point.x, point.y))


def ECPointGen(x: int, y: int, curve=curve.P256):
    return ECPoint(x, y, curve)


def AddECPoints(a: ECPoint, b: ECPoint):
    p1 = Point(a.x, a.y, a.curve)
    p2 = Point(b.x, b.y, b.curve)
    result = p1 + p2
    return ECPoint(result.x, result.y, result.curve)


def DoubleECPoints(a: ECPoint):
    p = Point(a.x, a.y, a.curve)
    double_p = 2 * p
    return ECPoint(double_p.x, double_p.y, double_p.curve)


def ScalarMult(k: int, a: ECPoint):
    p = Point(a.x, a.y, a.curve)
    result = k * p
    return ECPoint(result.x, result.y, result.curve)


def ECPointToString(p: ECPoint):
    return '0x{:x}, 0x{:x}, {}'.format(p.x, p.y, p.curve.name)


def StringToECPoint(s):
    curves_dict = {
        'P192': curve.P192,
        'P224': curve.P224,
        'P256': curve.P256,
        'P384': curve.P384,
        'P521': curve.P521,
        'W25519': curve.W25519,
        'W448': curve.W448,
        'secp192k1': curve.secp192k1,
        'secp224k1': curve.secp224k1,
        'secp256k1': curve.secp256k1,
        'brainpoolP160r1': curve.brainpoolP160r1,
        'brainpoolP192r1': curve.brainpoolP192r1,
        'brainpoolP224r1': curve.brainpoolP224r1,
        'brainpoolP256r1': curve.brainpoolP256r1,
        'brainpoolP320r1': curve.brainpoolP320r1,
        'brainpoolP384r1': curve.brainpoolP384r1,
        'brainpoolP512r1': curve.brainpoolP512r1,
    }
    value_arr = [value.strip() for value in s.split(',')]
    if len(value_arr) == 2:
        return ECPoint(int(value_arr[0], 16), int(value_arr[1], 16))
    elif len(value_arr) == 3:
        return ECPoint(int(value_arr[0], 16), int(value_arr[1], 16), curves_dict[value_arr[2]])
    else:
        print("Unable to convert string to ECPoint")


def PrintECPoint(p: ECPoint):
    print('X: 0x{:x}\nY: 0x{:x}\n(On curve <{}>)'.format(p.x, p.y, p.curve.name))
