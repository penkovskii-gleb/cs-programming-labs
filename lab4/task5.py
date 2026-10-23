god=2100
if god not in range(1,10000):
    print('ошибка')
elif(god//400==1)or (god//4==0 and god//100!=0):
    print('высокосный')
else:print('невысокосный')