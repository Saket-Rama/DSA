arr = [4, 2, 7, 2, 5, 4]
hash_table=[0]*13
for i in range(len(arr)):
    hash_table[arr[i]]+=1
    if hash_table[arr[i]]==2:
        print(arr[i])
        break