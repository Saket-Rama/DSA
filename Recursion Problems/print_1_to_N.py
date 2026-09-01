con=1
n=int(input())
def numbers(con,n):
    if con>n:
        return
    print(con)
    return numbers(con+1,n)
numbers(con,n)

# Recursion Tree - same as first problem and TC and SC too...