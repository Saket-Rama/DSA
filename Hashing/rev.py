arr = [1, 2, 2, 3, 4, 1, 5, 3]
hash_table=[0]*13
for i in range(len(arr)):
    hash_table[arr[i]]+=1
no_of_numbers=0
for i in range(len(hash_table)):
    if hash_table[i]>0:
        no_of_numbers+=1
print(no_of_numbers)