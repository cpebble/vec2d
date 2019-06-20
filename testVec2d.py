from vec2d import Vec2d
from math import radians

# Some helper utils
floatTol = 1E-10  # Ensure we get at least 10 digits of precision
tests = []


def Test(func):
    global tests
    tests += [(func.__name__, func)]


def isEqualWithTol(a, b):
    if a - b < floatTol and a - b > -floatTol:
        return True
    return False


def areVecEqual(a, b):
    xeq = isEqualWithTol(a.x, b.x)
    yeq = isEqualWithTol(a.y, b.y)
    return (xeq and yeq)


@Test
def testCreate():
    a = Vec2d(x=1, y=1)
    assert a.x == 1
    assert a.y == 1


@Test
def testAdd():
    a = Vec2d(x=1, y=1)
    b = Vec2d(x=1, y=1)
    c = a + b
    assert c.x == 2
    assert c.y == 2
    assert isinstance(c, Vec2d)

    d = a + 1
    assert d.x == 2
    assert d.y == 2
    assert isinstance(d, Vec2d)


@Test
def testSub():
    a = Vec2d(x=3, y=3)
    b = Vec2d(x=1, y=1)
    c = a - b
    assert c.x == 2
    assert c.y == 2
    assert isinstance(c, Vec2d)


@Test
def testMod():
    a = Vec2d(x=3, y=1)
    a = a % 2
    assert a.x == 1
    assert a.y == 1


@Test
def testMul():
    a = Vec2d(x=1, y=1)
    a = a*2
    assert a.x == 2
    assert a.y == 2


@Test
def testDiv():
    a = Vec2d(x=10, y=10)
    b = a/10
    assert areVecEqual(b, Vec2d(x=1, y=1))


@Test
def testRotate():
    a = Vec2d(x=1, y=0)
    b = a.rotate(radians(90))
    assert areVecEqual(b, Vec2d(0, -1))
    c = b.rotate(radians(90))
    assert areVecEqual(c, Vec2d(x=-1, y=0))
    d = c.rotate(radians(90))
    assert areVecEqual(d, Vec2d(x=0, y=1))
    e = d.rotate(radians(90))
    assert areVecEqual(a, e)


@Test
def testNormalize():
    a = Vec2d(x=2, y=0)
    assert a.normalize().length == 1
    assert areVecEqual(a.normalize(), Vec2d(x=1, y=0))


@Test
def testDotProduct():
    a = Vec2d(x=1, y=0)
    b = Vec2d(x=0, y=1)
    assert isEqualWithTol(a.dot_product(b), 0)
    assert isEqualWithTol(b.dot_product(a), 0)


if __name__ == "__main__":
    # Run the test
    total = len(tests)
    s, f = 0, 0
    for name, test in tests:
        print(f"Testing function: {name}")
        try:
            test()
            print("\tPASSED")
            s += 1
        except AssertionError as ex:
            print(f"Error in values\n{ex}")
            f += 1
        except Exception as ex:
            print(f"Error in running\n{ex}")
            f += 1
    print(f"""
SUMMARY:
########
Failures: {f}
Success: {s}
Succ/Total: {s}/{total}
""")
