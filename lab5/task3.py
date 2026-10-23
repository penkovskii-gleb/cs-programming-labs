n=int(input())
pol=0
otr=0
nol=0
for i in range(n):
    temp=float(input())
    if temp>0:
        pol=pol+1
    elif temp==0:
        nol=nol+1
    else:otr=otr+1
print('Ниже нуля: ',otr)
print('Равны нулю: ',nol)
print('Выше нуля: ',pol)
