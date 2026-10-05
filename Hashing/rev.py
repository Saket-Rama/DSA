s = "banana"
hash_table=[0]*26
for i in range(len(s)):
    hash_table[ord(s[i])-ord('a')]+=1
q=int(input())
while q>0:
    n=input()
    print(hash_table[ord(n)-ord('a')])
    q-=1