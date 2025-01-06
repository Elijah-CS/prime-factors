import numpy as np
import matplotlib.pyplot as plt

def get_log_diff(a,b):

    c = a * b
    a_log = np.log(a)
    c_s_log = np.log(np.sqrt(c))
    return float(c_s_log - a_log)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]


primeSize = 512
p = 12422160521539354950972405261644930617188546115135784299856216804262598374746363519064068304488324401297288137158417397964444100213248920933139268487305983
q = 13102400686731026620620607144506007577835792880009655217994874158729348390872980329048180249221990256946844587892499183078583850710968823924930657812567127
n = p * q
min = 1 << (primeSize - 1)
max = (1 << primeSize) - 1

x = []
y = []
z1 = []
z2 = []

for i in range(0, len(primes) - 1):
  for j in range(i + 1, len(primes)):

    x_val = primes[i]
    y_val = primes[j]
    z1_val = x_val * y_val
    z2_val = get_log_diff(primes[i], primes[j])

    x.append(x_val)
    y.append(y_val)
    z1.append(z1_val)
    z2.append(z2_val)

print(f"{len(x)} points")

fig = plt.figure()

ax1 = fig.add_subplot(1,1,1, projection='3d')
ax1.scatter(x, y, z1)

ax1.set_title('Product Difference')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.set_zlabel('Z Label')



# ax2 = fig.add_subplot(1,1,1, projection='3d')
# ax2.scatter(x, y, z2)

# ax2.set_title('Log Difference')
# ax2.set_xlabel('X Label')
# ax2.set_ylabel('Y Label')
# ax2.set_zlabel('Z Label')


tuples = list(zip(x,y,z1))
tuples.sort(key=lambda item: item[2])

for i in range(0, len(tuples)):
   
   item = tuples[i]

   a = item[0]
   b = item[1]
   c = item[2]
   print(f"{c}: -> ({a},{b})")

plt.show()