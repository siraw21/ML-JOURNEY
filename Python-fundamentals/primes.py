
# import math
# import time


# start_time = time.perf_counter()

# count = 0
# total = 0
# number = 100000


# def is_prime(num):
#     for i in range(2, math.isqrt(num) + 1):
#         if num % i == 0:
#             return False
#     return True


# for i in range(2, number):
#     if is_prime(i):
#         count += 1
#         total += i


# print("Trial Division")
# print("Count:", count)
# print("Sum:", total)

# end_time = time.perf_counter()

# execution_time = end_time - start_time

# print(f"Execution time: {execution_time:.6f} seconds")

import math
import time


start_time = time.perf_counter()

number = 1000000

# Assume every number is prime initially
is_prime = [True] * number

# 0 and 1 are not prime
is_prime[0] = False
is_prime[1] = False


for p in range(2, math.isqrt(number) + 1):

    if is_prime[p]:

        
        for multiple in range(p * p, number, p):
            is_prime[multiple] = False


count = 0
total = 0

for i in range(2, number):
    if is_prime[i]:
        count += 1
        total += i


print("Sieve of Eratosthenes")
print("Count:", count)
print("Sum:", total)

end_time = time.perf_counter()

execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")