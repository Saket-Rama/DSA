"""
Q9. Check whether two arrays have the same frequencies

Given:

arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 3, 2, 1]

Check whether both arrays contain the same numbers with the same frequencies.

Expected:

True

Don't compare them by sorting.

Use frequency arrays.
"""
arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 3, 2, 1]
h1=[0]*13
h2=[0]*13
for i in range(len(arr1)):
    h1[arr1[i]]+=1
for i in range(len(arr2)):
    h2[arr2[i]]+=1
same=True
for i in range(len(h1)):
    if h1[i]!=h2[i]:
        same=False
print(same)