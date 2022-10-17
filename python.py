import math
print("x**3 +4*x**2-10")
def f(x):
    return x**3 +4*x**2-10
def bisection(a,b,n):
    i=1
    while i<100:
        x = (a + b) / 2
        g=f(x)
        print("g: ",g)
        if f(a)*g<0:
            b=x
        else:
            a=x
        print(f"iterasyon num: {i} x={x} f(x): {f(x)}")
        i = i + 1
        if abs(a-b)<n:
            breakgşt
    print(f"x: {x}")
a=float(input("Alt aralik: "))
b=float(input("Üst aralik: "))
n=float(input("ε: "))
if f(a)*f(b)>=0:
    print("hata")
else:
    bisection(a,b,n)




