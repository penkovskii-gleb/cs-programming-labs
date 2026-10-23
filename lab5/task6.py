n = int(input().strip())
odd_count = 0
for r in range(n):
    row = []
    c = 1
    for k in range(r + 1):
        row.append(c)
        if c % 2 != 0:
            odd_count += 1
        c = c * (r - k) // (k + 1)
    print(" ".join(map(str, row)))
print(f"Нечетных элементов: {odd_count}")