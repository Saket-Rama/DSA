arr=[2,4,2,1,3,4,2]
q=[2,4,5,1]
hash_table=[0]*13
for i in range(n):
    hash_table[arr[i]]+=1
for i in q:
    print(hash_table[i])  