arr = [1, 2, 1, 3, 2, 4, 1]
hash_table=[0]*13
for i in range(len(arr)):
    hash_table[arr[i]]+=1
q=int(input())
while q>0:
    num=int(input())
    print(f"{num} and its frequency is {hash_table[num]}")
    q-=1