lst = []

print("Enter the number of elements in list: ")

n = int(input())

for i in range(0,n):

    ele = input()
    lst.append(ele)

lst.reverse()

print(lst)