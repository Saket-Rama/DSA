# why are the dicts used because a array can be of 10^7 not more than that and waste unnecessary memory...
"""
Number Hashing...
n=int(input("Enter the range of the array\n"))
arr=list(map(int,input("Enter the Elements\n").split(" ")))
# Pre-compute
hash_map={}
for n in arr:
    hash_map[n]=hash_map.get(n,0)+1
q=int(input("Enter the number of queries\n"))
while q>0:
    num=int(input("Enter the number\n"))
    #fetch
    print(hash_map.get(num,0))
    # Here the 0 is a default value if the number is present in the array it returns its frequency and if not returns 0...
    q-=1
# Storing and Fetching the data uses log(N) for best,average and worst case...
"""
"""
character hashing...
"""
st="abcadeghij"
#pre-compute...
hmp={}
for n in st:
    hmp[n]=hmp.get(n,0)+1
q=int(input("Enter the Queries\n"))
while q>0:
    ch=input("Enter the character\n")
    #fetch...
    print(hmp.get(ch,0))
    q-=1