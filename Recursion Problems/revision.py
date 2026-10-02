s=1
e=5
def f(i,n):
    if i>n:
        return
    f(i+1,n)
    print(i)
f(s,e)