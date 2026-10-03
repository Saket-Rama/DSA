"""
character hashing using brute force approach
"""
"""
s="abcabcefc"
n=input()
c=0
for alphabet in s:
    if n==alphabet:
        c+=1
else:
    print("Not Found")
print(c)
"""
# The program take O(n*N) for time complexity and it takes about 100s to execute which is not optimal and we need a hashing concept for the same...
# Using Hashing this is for smaller cases...
st=input("Enter the String\n")
q=int(input("Enter the Number of Queries:\n"))
# Precompute
hash_table=[0]*26
for i in range(len(st)):
    hash_table[ord(st[i])-ord('a')]+=1
while q>0:
    c=input("Enter the character\n")
    # fetch
    print(hash_table[ord(c)-ord('a')])
    q-=1