import random
import sys
import itertools

def random_generator(power=100):
    """
    Returns a random generator for U(3^power), where power defaults to 100.

    There is a theorem that says if g is a generator of a group of order n,
    then every k > 1 that satisifies gcd(k, n) = 1 will be a generator of
    the group.

    Note that |U(3^k)| = 3^(k-1) * 2. For example, |U(3)| = 3^0 * 2 = 2,
    |U(9)| = 3^1 * 2 = 6, |U(27)| = 3^2 * 2 = 18.
    This means that |U(3^100)| = 3^99 * 2.

    We also know that 2 is a generator for U(3^100), so our theorem states
    that for every k > 1 that satisfies gcd(k, 3^99 * 2) = 1, 2^k will be a
    generator of the group.

    Now, we notice that gcd(k, 3^99 * 2) = 1 whenever the number is not a
    multiple of 2 or 3. As a result, we just enumerate through the numbers.
    """
    n = pow(3,power - 1) * 2
    m = pow(3,power)

    # Iterate until we find a satisfying k
    while True:
        # Include 1 because we might have 2 as a generator
        k = random.randint(1, n)

        # gcd(k, 3^99 * 2) = 1 if not divisible by 3 or 2
        if k % 2 != 0 and k % 3 != 0:
            # Return 2^k mod 27
            return pow(2, k) % m

    # On failure, return -1
    return -1

if __name__ == '__main__':
    """
    Generates a random generator for U(3^100)
    """

    # num args and args
    num_args = len(sys.argv)
    if num_args != 1 and num_args != 2:
        print 'usage: python p5a.py <opt: exponent>'
    elif num_args == 1:
        print '>>>> Note: If this is slow, try doing python p5a.py <opt: exponent> to try a lower power than 3^100'
        gen = random_generator()
        print gen
    elif num_args == 2:
        print '>>>> Exponent: ', int(sys.argv[1])
        gen = random_generator(int(sys.argv[1]))
        print gen



