#task1
def squares(n):
    for i in range(n+1):
        yield i**2
n = int(input())
for square in squares(n):
    print(square, end=" ")

#task2
def even_numbers(n):
    for i in range(0,n+1,2):
        yield i
n = int(input())
print(",".join(map(str, even_numbers(n))))

#task3
def numbers(n):
    for i in range(n + 1):
        if i%3==0 and i%4==0:
            yield i
n = int(input())
print(list(numbers(n)))

#task4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a = int(input())
b = int(input())
for sq in squares(a, b):
    print(sq)

#task5
def nums(n):
    for i in range(n,-1,-1):
        yield i
n = int(input())
for num in nums(n):
    print(num)
