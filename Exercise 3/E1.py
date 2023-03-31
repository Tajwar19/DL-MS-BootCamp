#Keep the first, middle, and last characters of an input string

def func(st):

    st1 = ""

    if len(st)%2 == 1:
        b = int((len(s)-1)/2)
        st1 += st[b]
    else:
        a = int(len(st)/2)
        st1 += st[a-1]
        st1 += st[a]

    return st1

s = input()

print("First Character is: ",s[0])
print("Middle Character is: ",func(s))
print("Last Character is: ",s[len(s)-1])
    



