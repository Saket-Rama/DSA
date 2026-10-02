"""
Brute force approach to find the count of the number is ...
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