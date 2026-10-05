arr = [1, 3, 2, 3, 4, 3, 2, 1]
hash_table=[0]*13
for i in range(len(arr)):
    hash_table[arr[i]]+=1
max=0
for i in range(len(hash_table)):
    if max<hash_table[i]:
        max = hash_table[i]
print(max)