import sys
import mmi

def euclids(x, y):
    """
    finds the largest common divisor of two integers using
    euclids division algorithm
    """
    while y:
        x, y = y, x % y
    return x

def crt(m, a):
    # safety checks
    if len(m) < 1 or len(a) < 1 or len(m) != len(a):
        print "invalid m or a"
        return

    # check if co-prime
    for i in xrange(len(m)):
        for j in xrange(i + 1, len(m)):
            x = m[i]
            y = m[j]
            # to check if co-prime, check if gcd > 1
            gcd = euclids(x, y)
            if gcd > 1:
                print x, " and ", y, " are not relatively prime"
                return

    # calculate product of m_i's
    product = m[0]
    for i in xrange(1, len(m)):
        product *= m[i]

    total = 0
    # crt
    for i in xrange(len(m)):
        m_i = m[i]
        a_i = a[i]
        t = product / m_i
        total += a_i * mmi.mult_mod_inverse(t, m_i) * t
    return total % product

# example found from:
# http://gauss.math.luc.edu/greicius/Math201/Fall2012/Lectures/ChineseRemainderThm.article.pdf
if __name__ == '__main__':
    # num args and args
    num_args = len(sys.argv)
    if num_args != 1:
        print 'usage: python p6.py'
    else:
        m = [5, 7, 9, 11]
        a = [1, 2, 3, 4]
        print crt(m, a)


