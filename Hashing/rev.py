arr = [2, 4, 2, 1, 3, 4, 2]
queries = [2, 4, 5, 1]
hash_table=[0]*13
for i in range(len(arr)):
    hash_table[arr[i]]+=1
for q in queries:
    print(hash_table[q])