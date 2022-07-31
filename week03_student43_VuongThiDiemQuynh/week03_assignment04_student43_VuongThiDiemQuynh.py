'''import sympy

def fib(n):
    fibonacci_number = fibonacci(n)

if 0 == 0:
    print(fib(8)) #21
    print(fib(1)) #1'''

###################################

def fibonacci_number(n):
    if n == 0 or n == 1:
        return n
    else:
        f0 = 0
        f1 = 1
        fn = 0
        while n >= 2:
            fn = f0 + f1
            f0 = f1
            f1 = fn
            n -= 1
        return fn

if 0 == 0:
    print(fibonacci_number(8)) #21
    print(fibonacci_number(9)) #34
    print(fibonacci_number(10)) #55