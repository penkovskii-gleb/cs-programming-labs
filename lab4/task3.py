x=-4
y=7
if x == 0 and y == 0:
    print('Начало координат')
elif x != 0 and y == 0:
    print('Ось Х')
elif x == 0 and y != 0:
    print('Ось У')
elif x > 0 and y > 0:
    print('I четверть')
elif x < 0 and y > 0:
    print('II четверть')
elif x < 0 and y < 0:
    print('III четверть')
elif x > 0 and y < 0:
    print('IV четверть')