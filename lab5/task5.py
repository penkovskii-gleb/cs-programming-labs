cost=input()
num=0
obcost=0
while cost!='stop':
    num=num+1
    obcost=obcost+int(cost)
    cost=input()
print('Покупок: ',num)
print('Общая стоимость: ',obcost,' руб')
print(f'Средняя стоимость: {(obcost/num):.2f} руб')