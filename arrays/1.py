import numpy as np
a = np.array([1,2,3,4])

def print_array(nums):
    for num in nums:
        print(num)

print_array(a)
print(sum(a))
mult_array = np.multiply(a,3)
print(mult_array)