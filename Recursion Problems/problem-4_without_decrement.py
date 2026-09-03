def f(i,n):
    if i>n:
        return
    f(i+1,n)
    print(i)
f(1,5)
#Recursive Tree - f()