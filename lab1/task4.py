print("Введите длину поездки в секундах")
x = abs(int(input()))
sec = x%60
min = x//60%60
h = x//3600
print(f"Время {h:02d}:{min:02d}:{sec:0.2d}")
