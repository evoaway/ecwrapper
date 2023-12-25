# Project information
Elliptic curve wrapper

# Description
This is a working wrapper for using a library that works with algebra on elliptic curves. A library was used [fastecdsa](https://github.com/AntonKueltz/fastecdsa/tree/main). You can use pip: `$ pip install fastecdsa`
The wrapper contains two classes and several methods that implement basic tasks for working with elliptic curves and points on them.
* `class ECpoint` - a point on a curve containing coordinates and the curve on which it lies
* `class Curve` - elliptic curve, creates an elliptic curve from the library
* `BasePointGGet()` - returns the base point G of the curve
* `IsOnCurveCheck` - checks if the point lies on the curve\
Operations with points:
* `ECPointGen` - generates a new point by coordinates
* `AddECPoints` - returns the sum of two points 
* `DoubleECPoints` - returns the double point
* `ScalarMult` returns the result of scalar multiplication of a point by a scalar\
Functions with string:
* `ECPointToString` - convert point to string
* `StringToECPoint` - convert string to point
* `PrintECPoint` - print point

# Usage
Import wrapper
```python
from ecwrapper import *
```
Example check
```python
import random
from ecwrapper import *
    curve = Curve()
    G = curve.BasePointGGet()
    k = random.getrandbits(256)
    d = random.getrandbits(256)

    H1 = ScalarMult(d, G)
    H2 = ScalarMult(k, H1)

    H3 = ScalarMult(k, G)
    H4 = ScalarMult(d, H3)
    H4 == H3
```