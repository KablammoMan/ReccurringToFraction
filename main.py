import math

def euclid(n, d):
    if n % d == 0:
        return d
    else:
        return euclid(d, n%d)


def simplify(n, d):
    factors = 0
    while n > d:
        factors += 1
        n -= d
    hcf = euclid(n,d)
    new_n = int(n / hcf)
    new_d = int(d / hcf)
    return f"{factors} {new_n}/{new_d}"


num = input("Number: ")

rec = int(input("Length: "))
recp = num[(len(num)-rec):]

dif = len(num.split(".")[1]) - rec
fy = 10 ** dif
fx = fy * float(num)
print(f"{fy}x = {fx}")
ly = fy * (10 ** rec)
lx = fx * (10 ** rec)
print(f"{ly}x = {int(lx)}.{recp}")
n = int(lx - int(fx))
d = int(ly - fy)
print(f"x = {n}/{d}")
print(f"x = {simplify(n, d)}")