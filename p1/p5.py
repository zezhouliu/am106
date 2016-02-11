import sys

def extended_euclids(a, b):
    """
    extends euclids division algorithm by solving for m, n where
    gcd(a, b) = m*a + n*b
    """
    prevx = 1
    x = 0
    prevy = 0
    y = 1
    while b:
        q = a / b
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        a, b = b, a % b
    return prevx, prevy

if __name__ == '__main__':
    # num args and args
    num_args = len(sys.argv)
    if num_args != 3:
        print 'usage: python p5.py x y'
    else:
        print extended_euclids(int(sys.argv[1]), int(sys.argv[2]))

