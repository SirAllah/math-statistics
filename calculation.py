from math import sqrt
from numpy import zeros, ones, hstack, random, nonzero


def probability(x, num_exp):
    for i in x:
        x[i] /= num_exp
    return x

def calculation(num_exp):
    
    expected_math = 0
    expected_mathematical_pow2 = 0
    prob = {i:0 for i in range(1, 35)}

    a = ones(4, bool)
    b = zeros(32, bool)
    place_tuze = hstack([a,b])
    for _ in range(num_exp):
        random.shuffle(place_tuze)
        term = nonzero(place_tuze == True)[0][0] + 1

        expected_math += term
        expected_mathematical_pow2 += term ** 2
        prob[term] += 1

    expected_math /= num_exp
    expected_mathematical_pow2 /= num_exp
    disp = expected_mathematical_pow2 - expected_math ** 2
    prob = probability(prob, num_exp)

    res = ("M[x] = \t" + "%0.6f" % (expected_math) + "\n")
    res += ("D[x] = \t" + "%0.6f" % (disp) + "\n")
    res += ("σ = \t" + "%0.6f" % (sqrt(disp)))

    return res, prob