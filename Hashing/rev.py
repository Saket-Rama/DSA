n=int(input())
arr=list(map(int,input().split(" ")))
hmp={}
for n in arr:
    hmp[n]=hmp.get(n,0)+1
q=int(input())
while q>0:
    num=int(input())
    print(hmp.get(num,0))
    q-=1