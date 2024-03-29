'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#Python implementation of Max prime factor using a refined sieve.

import math

def max_prime_factor(n): 
    maxPrime = -1
    
    # We keep dividing n by 2 to get rid of all the even composite factors.
    while n % 2 == 0: 
        maxPrime = 2
        n //= 2 # equivalent to n //= 2

    # We loop over the possible odd factors.
    # to remove the rest of the composites, and updating maxPrime to the largest factor.
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        
        while n % i == 0: 
            maxPrime = i 
            n //= i #assign quotient of n/i to n
    
    # If at this stage n is is still bigger than 2
    # then n must be prime so we return it, otherwise we return maxPrime
    return n if n > 2 else maxPrime
  


N = 600851475143
print(max_prime_factor(N))