#Create a function that can add unlimited numbers (arguments)

def add(*arg):

    sum = 0

    for i in arg:
        sum += i

    return sum

l = [1,2,3,4,5,6,7,8,9,10]

print(add(*l))