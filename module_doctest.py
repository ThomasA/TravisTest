"""
This is the "somemodule" module. It contains a function, square(),
that calculates and returns its input squared. For example,

>>> square(3)
9

It also contains a function, half(), that calculates and returns half
of its input (as a float). For example,

>>> half(3)
1.5
"""

def square(x):
    return x**2

def half(x):
    return float(x)/2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
