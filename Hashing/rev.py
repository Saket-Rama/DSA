arr = [1, 2, 3, 2, 4, 1, 5]
hash_table=[0]*13
for i in range(len(arr)):
    hash_table[arr[i]]+=1
for i in range(len(arr)):
    if hash_table[arr[i]]==1:
        print(arr[i],end=' ')