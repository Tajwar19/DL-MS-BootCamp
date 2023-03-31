#Arrange string characters such that lowercase letters should come first

def arrange(st):
    st1 = ""
    st2 = ""

    for i in st:
        if (i.isupper()) == True:
            st1 += i
        else:
            st2 += i
    
    st = st2+st1
    return st

s = input()

print(arrange(s))