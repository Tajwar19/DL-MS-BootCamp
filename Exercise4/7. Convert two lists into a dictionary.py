keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res1 = {}

for i in keys:
    for j in values:
        res1[i] = j
        values.remove(j)
        break

print(res1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res2 = dict(zip(keys,values))

print(res2)