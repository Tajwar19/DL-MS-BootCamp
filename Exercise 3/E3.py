#Count all letters, digits, and special symbols from a given string. [Hint: Use isalpha() and isdigit() 

def counting_letter(s):

    count = 0

    for i in s:
        if (i.isalpha()) == True:
            count += 1

    return count

def counting_digit(s):

    count = 0

    for i in s:
        if (i.isdigit()) == True:
            count += 1

    return count

def counting_Special_Symbol(s):

    count = 0

    for i in s:
        if (i.isalpha()) == True:
            count += 1
        elif(i.isdigit()) == True:
            count += 1
    
    leng = int(len(s))

    return (leng - count)

s = input()

print("Chars: ",counting_letter(s))
print("Digts: ",counting_digit(s))
print("Symbols: ",counting_Special_Symbol(s))