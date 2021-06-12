from math import sqrt
from random import shuffle


def probability(x, num_exp):
    for i in x:
        x[i] /= num_exp
    return x

def calculation(num_exp):
    expected_math = 0
    expected_mathematical_pow2 = 0
    x = {i:0 for i in range(1, 35)}

    place_tuze = [True for _ in range(4)] + [False for _ in range(32)]
    for i in range(num_exp):

        shuffle(place_tuze)
        term = place_tuze.index(True) + 1

        expected_math += term
        expected_mathematical_pow2 += term ** 2
        x[term] += 1

    expected_math /= num_exp
    expected_mathematical_pow2 /= num_exp

    prob = probability(x, num_exp)

    res = ("M[x] = \t" + "%0.6f" % (expected_math) + "\n")
    disp = expected_mathematical_pow2 - expected_math ** 2
    res += ("D[x] = \t" + "%0.6f" % (disp) + "\n")
    res += ("σ = \t" + "%0.6f" % (sqrt(disp)))

    return res, prob