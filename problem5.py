'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

import math 

n = 20 
ans = 1
for i in range(1, n + 1): 
  ans = (ans * i)//math.gcd(ans, i)
  
print(ans)
  
