"""
Find Missing Number — Medium

Given numbers from 1 to 10, with one number missing:

arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]

Find the missing number.

Expected:

5
"""
arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
hash_table=[0]*13
missing_number=0
for i in range(len(arr)):
    hash_table[arr[i]]+=1
for i in range(len(arr)):
    if hash_table[i]==0:
        missing_number=i
print(missing_number)