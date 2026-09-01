def f():
    print(1)
    f()
print(f())
# Stack overflow problem is based on this problem because we use recursion concept and we didn't end it so it stops the program after several outputs...