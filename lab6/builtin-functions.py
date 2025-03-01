#task1
from functools import reduce
def mult(numbers):
    return reduce(lambda x, y: x * y, numbers)
numbers = list(map(int,input().split()))
print(mult(numbers))

#task2
def count_up_low(s):
    count_up = sum(map(str.isupper, s))
    count_low = sum(map(str.islower, s))
    return count_up, count_low
s = input()
print(count_up_low(s))

#task3
def palindrome(s):
    if(s==s[::-1]):
        print(s,"is palindrome")
    else:
        print(s,"is not palindrome")
s = input()
palindrome(s)

#task4
import math
def square(n,t):
    print("Square root of",n,"after",t,"miliseconds is",math.sqrt(n))
n = int(input())
t = int(input())
square(n,t)

#task5
def elements(t):
    return all(t)
tuple1 = (True, 1, "Hi")
tuple2 = (True, 0, "Hello")
print(elements(tuple1))  
print(elements(tuple2)) 