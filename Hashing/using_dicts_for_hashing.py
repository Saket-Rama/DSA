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