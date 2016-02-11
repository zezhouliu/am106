import sys
import p5

def mult_mod_inverse(n, p):
    '''
    Applies the extended euclids in order to calculate the
    multiplicative modular inverse.
    returns x such that n * x = 1 mod p
    '''
    r1, r2 = p5.extended_euclids(n, p)
    if r1 < 0:
        r1 = r1 + p
    return r1

if __name__ == '__main__':
    # num args and args
    num_args = len(sys.argv)
    if num_args != 3:
        print 'usage: python p6.py n p'
    else:
        print mult_mod_inverse(int(sys.argv[1]), int(sys.argv[2]))


