lst1 = []
lst2 = []

print("Enter the number of element of set A: ")
n1 = int(input())

print("Now enter the element of set A: ")

for i in range(0,n1):
    a = input()
    lst1.append(a)

print("Enter the number of element of set B: ")
n2 = int(input())

print("Now enter the element of set B: ")

for i in range(0,n2):
    b = input()
    lst2.append(b)

for x in lst1:
    for y in lst2:
        if x == y:
            lst1.remove(x)
            lst2.remove(y)

set1 = set(lst1)
set1.update(lst2)

print(set1)