st=input()
q=int(input())
hash_table=[0]*26
for i in range(len(st)):
    hash_table[ord(st[i])-ord('a')]+=1
while q>0:
    c=input()
    print(hash_table[ord(c)-ord('a')])
    q-=1