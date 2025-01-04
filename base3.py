def decimal_to_base3(n):
  """Converts a decimal number to base 3."""
  if n == 0:
    return "0"
  result = ""
  while n > 0:
    result = str(n % 3) + result
    n //= 3
  return result

# print(decimal_to_base3(10))  # Output: 101
# print(decimal_to_base3(20))  # Output: 202


def base3_to_base10(num_str):
  """
  Converts a base-3 number (represented as a string) 
  to base-10.
  """

  result = 0
  power = 0

  for digit in num_str[::-1]:  # Iterate through digits from right to left
    result += int(digit) * (3 ** power)
    power += 1

  return result

# print(base3_to_base10("0001"))
# print(base3_to_base10("0002"))
# print(base3_to_base10("0011"))
# print(base3_to_base10("0012"))
# print(base3_to_base10("0021"))
# print(base3_to_base10("0022"))

# print(base3_to_base10("1001"))
# print(base3_to_base10("1102"))
# print(base3_to_base10("1111"))
# print(base3_to_base10("1112"))
# print(base3_to_base10("1121"))
# print(base3_to_base10("1122"))

import itertools
# a = [1,3,7,9]
a = [0,1,2,3,4,5,6,7,8,9]
lst = list(itertools.product(a, repeat=2))

print(lst)