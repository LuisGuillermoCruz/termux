import numpy as np

a = [[1,2,
      3,4]]

print(a)

print(np.shape(a))

input()


for i in range(5,-1,-1):
   # print(i)
    for j in range(0,i):
        print("*", end="")
    print()
