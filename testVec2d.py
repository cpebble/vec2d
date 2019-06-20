from vec2d import Vec2d

# Some helper utils
floatTol = 1E-6
tests = []


def Test(func):
    global tests
    tests += [func]


@Test
def isEqualWithTol(a, b):
    if a - b < floatTol and a - b > -floatTol:
        return True
    return False


@Test
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
    print("Not implemented")
    pass


@Test
def testMul():
    print("Not implemented")
    pass


@Test
def testDiv():
    print("Not implemented")
    pass


@Test
def testRotate():
    print("Not implemented")
    pass


@Test
def testNormalize():
    print("Not implemented")
    pass


@Test
def testDotProduct():
    print("Not implemented")
    pass


if __name__ == "__main__":
    # Run the test
    for test in tests:
        test()
