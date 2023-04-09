def isnotempty(em):
    if em != " ":
        return True
    else:
        return False

lst = ["Code", " ", "Studio", "Academy", " "]

f = filter(isnotempty,lst)

print(list(f))

