import math
print("x**3 - 2*(x*2) -5")
def f(x):
    return x**3 -2*(x**2)-5
def bisection(a,b,n):
    i=1
    x=0
    kontrol=True
    while i<100:
        x = (a + b) / 2
        if f(x)<0:
            a=x
        else:
            b=x
        print("İ.t: ",i,"X: ",x,"F(x): ",f(x))
        if i==n:
            kontrol=False
            quit()
        kontrol=True
        i=i+1
    print("Kök: ", x)
a=float(input("Alt aralik: "))
b=float(input("Üst aralik: "))
n=float(input("İ.t: "))
if f(a)*f(b)>0:
    print("hata")
else:
    bisection(a,b,n)
