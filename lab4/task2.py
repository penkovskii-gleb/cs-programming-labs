cost=1800
age=16
if age in range (0,121):
    if age<6:
        print("Стоимость: 0.00 руб")
    elif age<18:
        print(f'Стоимость: {cost/2:.2f} руб')
    elif age<60:
        print(f'Стоимость: {cost:.2f} руб')
    elif age<121:
        print(f'Стоимость: {cost/10*7:.2f} руб')