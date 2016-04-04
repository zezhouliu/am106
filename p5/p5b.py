import random
import sys
import itertools

import p5a

def diffie_helman(g):
    """
    Given a public g, it computes a private a (and b) in order to demonstrate
    the Diffie-Helman key exchange.
    """
    power = 15
    n = pow(3,power - 1) * 2

    a = random.randint(1, n)
    b = random.randint(1, n)
    print "User 1 generated a: ", a
    print "User 2 generated b: ", b

    ga = pow(g, a) % n
    print "User 1 sends g^a: ", ga
    gb = pow(g, b) % n
    print "User 2 sends g^b: ", gb

    gba = pow(gb, a) % n
    print "User 1 arrives at (g^b)^a: ", gba
    gab = pow(ga, b) % n
    print "User 2 computes (g^a)^b: ", gab

if __name__ == '__main__':
    """
    Implements Diffie-Helman
    """

    # num args and args
    num_args = len(sys.argv)
    if num_args != 1 and num_args != 2:
        print 'usage: python p5b.py <opt: exponent>'
    elif num_args == 1:
        print '>>>> Note: If this is slow, try doing python p5b.py <opt: exponent> to try a lower power than 3^100'
        gen = p5a.random_generator()
        print "g = ", gen
        diffie_helman(gen)
    elif num_args == 2:
        print '>>>> Exponent: ', int(sys.argv[1])
        gen = p5a.random_generator(int(sys.argv[1]))
        print "g = ", gen
        diffie_helman(gen)


