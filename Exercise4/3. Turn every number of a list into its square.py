
lst = []

print("Enter the number of elements: ")
n = int(input())

for i in range(0,n):
    ele = int(input())
    lst.append(ele)

square = lambda a:a*a
m = map(square,lst)

print(list(m))

sq = map(lambda a : a*a, lst)

print(list(sq))
