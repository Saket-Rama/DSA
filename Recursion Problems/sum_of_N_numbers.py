"""
# paremeter based solution...
"""
# Sum of n natural numbers is n*((n+1)/2)
"""
i=5
def sum(n,i):
    if i<1:
        print(n)
        return
    return sum(n+i,i-1)
sum(0,i)
"""
"""
Functional Based Solution
"""
n=5
def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(n))