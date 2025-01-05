import mpmath

def print_diff(a,b):
    """
    As distance between a and b increases, this value increases
    """
    c = a * b
    a_log = mpmath.ln(a)
    b_log = mpmath.ln(b)
    c_s_log = mpmath.ln(mpmath.sqrt(c))
    print(c_s_log - a_log)
    print()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]

for i in range(0, len(primes) - 1):
  print(f"i = {i}")
  for j in range(i + 1, len(primes)):
    print_diff(primes[i], primes[j])