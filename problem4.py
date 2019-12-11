'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

lowerLimit = 100
upperLimit = 999
palindrome = 0

for i in range(upperLimit, lowerLimit, -1):
  for j in range(upperLimit, lowerLimit, -1):
    product = str(i*j)
    reversedProduct =''.join(reversed(product)) 
    if (reversedProduct == product and int(product) >= palindrome):
      palindrome = int(product)
    
print(palindrome)
  