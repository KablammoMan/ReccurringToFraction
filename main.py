import math


def simplify(n, d):
    nfacts = []
    dfacts = []
    hcf = 1
    for i in range(1, math.floor(math.sqrt(abs(n)))+1):
        if n % i == 0:
            nfacts.append(i)
            nfacts.append(n / i)
    for i in range(1, math.floor(math.sqrt(abs(d)))+1):
        if d % i == 0:
            dfacts.append(i)
            dfacts.append(d / i)
    for i in nfacts:
        if i in dfacts and i > hcf:
            hcf = i
    new_n = int(n / hcf)
    new_d = int(d / hcf)
    return f"{new_n}/{new_d}"


num = input("Number: ")

rec = int(input("Length: "))


fy = 10 ** (len(num.split(".")[1]) - rec)
fx = int(fy * float(num) * 100) / 100
print(f"{fy}x = {fx}")
ly = fy * (10 ** rec)
lx = fx * (10 ** rec)
print(f"{ly}x = {lx}")
n = int(lx - int(fx))
d = int(ly - fy)
print(f"x = {n}/{d}")
print(f"x = {simplify(n, d)}")