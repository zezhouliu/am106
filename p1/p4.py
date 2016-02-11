import sys

def euclids(x, y):
    """
    finds the largest common divisor of two integers using
    euclids division algorithm
    """
    while y:
        x, y = y, x % y
    return x

if __name__ == '__main__':
    # num args and args
    num_args = len(sys.argv)
    if num_args != 3:
        print 'usage: python p4.py x y'
    else:
        print euclids(int(sys.argv[1]), int(sys.argv[2]))
