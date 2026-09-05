"""
Reverse the array using list property
"""
"""
n=5
def reverse_array(self,arr:list,n:int)->None:
    return arr.reverse()
"""

"""
Brute Force Approach
"""
"""

def reverse_array(arr:list,n:int)->None:
    ar=[]
    arr.reverse()
    for i in arr:
        ar.append(i)
    print(ar)
n=4
reverse_array([1,2,3,4],n)
"""
"""
Two Pointer Technique
"""
def reverse_array(arr):
    p1=0
    p2=len(arr)-1
    while p1<p2:
        arr[p1],arr[p2] = arr[p2],arr[p1]
        p1+=1
        p2-=1
    arr2=list(arr)
    print(arr2)
reverse_array([1,2,3,4,5])