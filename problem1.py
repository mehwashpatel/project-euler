'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

upperLimit = 1000
lowerLimit = 3
multiplesArr = [3,5]
sum = 0

for i in range(lowerLimit, upperLimit):
  if (i%multiplesArr[0] == 0):
    sum = sum + i
  elif (i%multiplesArr[1] == 0):
    sum = sum + i

return (sum)