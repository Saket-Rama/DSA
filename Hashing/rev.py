"""
Find Duplicate Number — Medium

Given:

arr = [1, 3, 4, 2, 5, 3]

Find the number that appears more than once.

Expected:

3
"""
arr = [1, 3, 4, 2, 5, 3]
hash_table=[0]*13
more_than_once=0
for i in range(len(arr)):
    hash_table[arr[i]]+=1
for i in range(len(arr)+1):
    if hash_table[i]>1:
        more_than_once=i
print(more_than_once)