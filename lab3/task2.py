x = "  иВАНОВ иВАН иВАНОВИЧ"

x = x.strip().lower().title().split(" ")
x[1] = x[1][0] + "."
x[2] = x[2][0] + "."
x = " ".join(x)
print(x)
