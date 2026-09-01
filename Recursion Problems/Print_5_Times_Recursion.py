"""
count=0
def name(n):
    global count
    if count==5:
        return
    else:
        print(n)
        count+=1
    return name(n)

name("Saket")
"""

def name(count,n):
    if count>n:
        return
    print("Saket")
    return name(count+1,n)

count=1
n=int(input())
name(count,n)

# Recursion Tree f(1,4)->  f(2,4) -> f(3,4) -> f(4,4)...
# TC - O(n) and SC - O(n)