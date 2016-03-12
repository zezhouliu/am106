import sys
import p5a

if __name__ == '__main__':
    """
    Generates all elements of Sn
    """

    # num args and args
    num_args = len(sys.argv)
    if num_args != 2:
        print 'usage: python p5a.py <n>'
    else:
        n = int(sys.argv[1])
        perms = p5a.permutations(n)
        # Only examine the permutations with length == n
        full_length_perms = [x for x in perms if len(x) == n]
        sols = []
        for p in full_length_perms:
            found = True
            found2 = True
            # Check by looking at +-1 with next one
            # Check by looking at diagonals with future
            for i in xrange(n - 1):
                if found == False or abs(p[i] - p[i + 1]) == 1:
                    found = False
                    break
                else:
                    for j in xrange(i + 1, n):
                        if abs(p[i] - p[j]) == abs(i - j):
                            found = False
                            break
            if found:
                sols.append(p)

        print len(sols)


