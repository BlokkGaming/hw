res = []

n = int(input("кол-во элементов первого множества чисел: "))
m = int(input("кол-во элементов второго множества чисел: "))

nlist = []
mlist = [] 

for i in range(n):
    nlist.append(int(input(f'{i+1}-й эелемент первого множества числе: ')))
for k in range(m):
    mlist.append(int(input(f'{k+1}-й эелемент второго множества числе: ')))

for t in nlist:
    for y in mlist:
        if t == y:
            res.append(t)

res.sort()
print(res)