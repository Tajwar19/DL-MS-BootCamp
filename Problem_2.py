def largest_num(a,b,c):
    if a>b and a>c:
        maxi = a
    elif b>a and b>c:
        maxi = b
    else:
        maxi =  c

    return maxi


a = int(input()) 
b = int(input()) 
c = int(input()) 

largest_number = largest_num(a,b,c)

print("Largest number is: ",largest_number)
