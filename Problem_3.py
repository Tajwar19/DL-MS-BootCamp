def conderter(string):
    s = ""
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            s+= "1"
        else:
            s+= "0"
    return s


st = input()

print(conderter(st))