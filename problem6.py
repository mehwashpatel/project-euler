'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

""" Arithmetic Approach"""
def sum_square_difference(n):
  return (((n**2) * (n + 1)**2) / 4) - (n * (n + 1) * (2*n + 1) / 6)

print(sum_square_difference(100))

"""Brute Force"""
lowerLimit = 11
upperLimit = 101
sumSquare = 385
sum = 55

for i in range(lowerLimit, upperLimit):
  square = i**2
  sumSquare = sumSquare + square
  sum = sum + i

squareSum = sum ** 2

difference = squareSum - sumSquare
print(difference)

  
