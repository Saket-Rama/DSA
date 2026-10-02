"""
Brute force approach to find the count of the number is ...
"""
"""
n=int(input())
c=0
li=[1,2,3,4,3,5]
for i in li:
    if n==i:
        c+=1
else:
    print("Not Found")        
print(c)
"""
# The program take O(n*N) for time complexity and it takes about 100s to execute which is not optimal and we need a hashing concept for the same...
# Using hashing 
n=int(input("Enter the Length of the Array:\n"))
arr=list(map(int,input().split()))
hash_table=[0]*13
for i in range(n):
    hash_table[arr[i]]+=1
q=int(input("Enter the Number of Queries:\n"))
while q>0:
    num=int(input("Enter the number:\n"))
    print(hash_table[num])
    q-=1