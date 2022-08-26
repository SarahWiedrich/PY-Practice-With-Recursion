# 2. Write a function that prints the natural numbers from 1 to n.

def natural_numbers(x, number=1):
    if x > number:
        return 
    else:
        print(x) 
        natural_numbers(x, number + 1)  

natural_numbers(10)