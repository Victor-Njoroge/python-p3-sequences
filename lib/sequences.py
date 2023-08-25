#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_Array=[0,1]
    
    while len(fibonacci_Array) < length :
     newNum= fibonacci_Array[-1] + fibonacci_Array[-2]
     fibonacci_Array.append(newNum)
    print(fibonacci_Array)
print_fibonacci(9)