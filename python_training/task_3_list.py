
l1 = [5, 10, 15, 29, 25, 30, 35, 40]
print(l1[2], l1[-2])
print(l1[-4:-2])

l2 = ['one', 'two', 'three', 'four', 'five']

print(len(l2))

for l in l2:
    print(l, sep='*')

l2.append('six')

print(*l2)