# nums = list(range(1,100))
nums = list(range(1,50)) + list(range(101,150))

tuples = []

for i in range(0, len(nums) - 1):
  for j in range(i, len(nums)):
    a = nums[i]
    b = nums[j]
    c = a * b

    tuples.append((a,b,c))

# sorted_tuples = sorted(tuples, key=lambda x:x[2])
sorted_tuples = tuples

for item in sorted_tuples:
  a = item[0]
  b = item[1]
  c = item[2]

  print(f"{c} = ({a}, {b})")

x,y,z = zip(*sorted_tuples)

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import colors

# norm = colors.Normalize(vmin=z[0], vmax=z[-1])
norm = colors.Normalize(vmin=0,vmax=len(x))

fig = plt.figure()

ax = fig.add_subplot(1,1,1,projection='3d')

ax.scatter(x,y,z,c=list(range(len(x))), norm=norm)

ax.set_title("Products")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

# plt.show()
plt.savefig("file.png")
