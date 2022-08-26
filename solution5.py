# 5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def is_palindrome(str):
  if len(str) == 1 or len(str) == 0:
    return True
  else:
    return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print("is 'apple' a palindrome?")
print(is_palindrome('apple'))
print("is 'tacocat' a palindrome?")
print(is_palindrome('tacocat'))

# Bonus. Write a function that when given two numbers, finds their greatest common divisor.

def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

print("gcd of 15 and 10:",gcd(15,10))
print("gcd of 46 and 12:",gcd(46,12))