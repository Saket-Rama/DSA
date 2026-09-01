"""
def f():
    print(1)
    f()
print(f())
"""
# Stack overflow problem is based on this problem because we use recursion concept and we didn't end it so it stops the program after several outputs...

# In order to stop this infinite recursion i need a base condition...
"""
cut=0
def f():
    global cut
    if(cut==3):
        return
    print(cut)
    cut+=1
    return f()
f()
"""
