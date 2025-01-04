import util

primeSize = 512
p = util.getRandomPrime(primeSize)
q = util.getRandomPrime(primeSize)
while p == q:
    q = util.getRandomPrime(primeSize)

if p > q:
    tmp = p
    p = q
    q = tmp

n, e, d = util.getKeys(p, q)

import mpmath

print("n:  ", n)
print("p:  ", p)
print("q:  ", q)
print(f"max: {n // int(mpmath.power(2, primeSize - 1))}")
print(f"max: {int(mpmath.power(2, primeSize) - 1)}")
print("\n")

mpmath.mp.dps = 200

# result = mpmath.ln(q)
# print(result)

# result = mpmath.exp(result)
# print(result)

n_s = mpmath.sqrt(n)
print("sqrt(n): ", n_s)
print("\n")

p_log = mpmath.ln(p)
n_s_log = mpmath.ln(n_s)
q_log = mpmath.ln(q)


print(f"p_log: {p_log}")
print(f"n_s_log: {n_s_log}")
print(f"q_log: {q_log}")

print(f"n_s_log - p_log: {n_s_log - p_log}")
print(f"q_log - n_s_log: {q_log - n_s_log}")


print(f"math.exp(p_log): {(mpmath.exp(p_log))}")
print(f"math.exp(q_log): {(mpmath.exp(q_log))}")
print("\n")


# First 14 decimal points match. Maybe rely on that and then round?
# import math
# import random
# ending = random.randint(100, 999)
# new_num = ending * math.pow(10, -14)
# new_num += p_log
# print(new_num)
# # print('{:.17f}'.format(new_num))

# print(mpmath.exp(new_num))

# q = "9928691115225312690443933980740658060251319749127521426393286767902493742201479037503896194261000747440216861470611342987659601995026113339940994648216073"
# """
# 9928691115225437566788511259361075387631483313228184710648512318591353047673763278611343576194370818246621761530757414866125940849926562682586246760366080
# """

# import math

# result = math.log(int(q))
# print(result)

# result = math.exp(result)
# print(result)

# print("========================================")

# from decimal import Decimal, getcontext

# getcontext().prec = 175  # Set the desired precision
# x = Decimal(q)

# result = Decimal.ln(x)  # Use Decimal.ln for natural logarithm
# print(result)

# result = Decimal.exp(result)
# print(result)

# print("========================================")

# import mpmath

# mpmath.mp.dps = 175

# result = mpmath.ln(q)
# print(result)

# result = mpmath.exp(result)
# print(result)