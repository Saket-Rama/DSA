n=int(input())
arr=list(map(int,input().split(" ")))
hmp={}
for i in arr:
    hmp[i]=hmp.get(i,0)+1
print(hmp)