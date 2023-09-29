res = 0

nlist = []
k = 1

n = int(input('[n] введите кол-во кустов: '))
for i in range(n):
    nlist.append(int(input(f'введите кол-во ягод на {i+1}-ом кусте: ')))

while k != len(nlist)-1:
    if (nlist[k] + nlist[k-1] + nlist[k+1]) > res:
        res = (nlist[k] + nlist[k-1] + nlist[k+1])
print(res)