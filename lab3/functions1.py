#task1

grams = float(input())
def ounces(gram):
    return 28.3495231 * gram
print(ounces(grams))
#task2
def calcC():
    F = int(input())
    return (5 / 9) * (F - 32)
print(calcC())
#task3
heads = 35
legs = 94
def solve(numheads, numlegs):
    y = (numlegs-2*numheads)/2
    x = numheads-y
    return x,y
print(solve(heads,legs))

#task4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input().split()))
prime_numbers = filter_prime(numbers)
print(prime_numbers)

#task5
from itertools import permutations
def permutation(s):
    for perm in permutation(s):
        print("".join(perm))
user = input()
permutation(user)

#task6
def reverse(sentence):
    return " ".join(sentence.split()[::-1])
user = input()
print(reverse(user))

#task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))  

#task8
def spy_game(nums):
    lst = [0, 0, 7]
    index = 0
    for num in nums:
        if num == lst[index]:
            index += 1
        if index == len(lst):
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 

#task9
r = float(input())
def volume(r):
    return (4*3.14*r**3)/3
print(volume(r))

#task10
def unique(lst):
    uniquelst = []
    for num in lst:
        if num not in uniquelst:
            uniquelst.append(num)
    return uniquelst

lst = list(map(int, input().split()))
print(unique(lst))

#task11
str = input()
def pldm(str):
    if(str == str[::-1]):
        return "Palindrome"
    else:
        return "Not  Palindrome"
print(pldm(str))

#task12
def histogram(lst):
    for num in lst:
        print('*' * num)
lst = list(map(int, input().split()))
histogram(lst)

#task13
import random
def guess_number():
    random_number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    count = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        count += 1
        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
guess_number()

#task14
from functions2 import take_movie
