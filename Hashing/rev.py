n=int(input())
arr=list(map(int,input().split()))
hash_table=[0]*13
for i in range(n):
    hash_table[arr[i]]+=1
q=int(input())
while q>0:
    num=int(input())
    print(hash_table[num])
    q-=1