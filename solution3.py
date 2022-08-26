# 3. Write a function that returns the first n elements in the Fibonacci Sequence.

def nth_fibbonacci(n):
    if n<=0:
        print("Incorrect input")

    elif n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)
 
print("2nd fib number:")
print(nth_fibbonacci(2))
print("4th fib number:")
print(nth_fibbonacci(4))
print("8th fib number:")
print(nth_fibbonacci(8))