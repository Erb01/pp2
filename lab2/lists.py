thislist = ["apple", "banana", "cherry"]
print(thislist)
##
thislist1 = ["apple", "banana", "cherry"]
print(len(thislist1))
##
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
##
list4 = ["abc", 34, True, 40, "male"]
##
mylist2 = ['apple', 'banana', 'cherry']
print(mylist2[1])
##
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
##
thislist3 = ["apple", "banana", "cherry"]
if "apple" in thislist3:
  print("Yes, 'apple' is in the fruits list")
##
thislist4 = ["apple", "banana", "cherry"]
thislist4[1] = "blackcurrant"
print(thislist4)
##
thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist5[1:3] = ["blackcurrant", "watermelon"]
print(thislist5)
##
thislist6 = ["apple", "banana", "cherry"]
thislist6.insert(2, "watermelon")
print(thislist6)
##
thislist7 = ["apple", "banana", "cherry"]
thislist7.append("orange")
print(thislist7)
##
thislist8 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist8.extend(tropical)
print(thislist8)
##
thislist9 = ["apple", "banana", "cherry"]
thislist9.remove("banana")
print(thislist9)
##
thislist10 = ["apple", "banana", "cherry"]
thislist10.pop(1)
print(thislist10)
##
thislist11 = ["apple", "banana", "cherry"]
del thislist11[0]
print(thislist11)
##
thislist12 = ["apple", "banana", "cherry"]
thislist12.clear()
print(thislist12)
##
thislist13 = ["apple", "banana", "cherry"]
for i in range(len(thislist13)):
  print(thislist13[i])
##
thlist = ["apple", "banana", "cherry"]
i = 0
while i < len(thlist):
  print(thlist[i])
  i = i + 1
##
thilist = ["apple", "banana", "cherry"]
[print(x) for x in thilist]
##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
##
thislist14 = [100, 50, 65, 82, 23]
thislist14.sort()
print(thislist14)
thislist14.sort(reverse = True)
print(thislist14)
##
def myfunc(n):
  return abs(n - 50)

thislis = [100, 50, 65, 82, 23]
thislis.sort(key = myfunc)
print(thislis)
##
thislist15 = ["apple", "banana", "cherry"]
mylist = thislist15.copy()
print(mylist)
##
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
##
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)