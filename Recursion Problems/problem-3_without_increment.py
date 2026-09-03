n=int(input())
def natural(i):
    if i<1:
        return
    natural(i-1)
    print(i)
natural(n)
# Recursion Tree - natural(5)-> natural(4)-> natural(3)-> natural(2)->natural(1)...
#But we have print() statement afterwards returning the function so the recursion goes on till last iteration and print the iteration in reverse order...