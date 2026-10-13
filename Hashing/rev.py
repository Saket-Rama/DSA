s = "banana"
queries = ['a', 'b', 'n', 'z']
hmp={}
for i in s:
    hmp[i]=hmp.get(i,0)+1
for i in queries:
    print(hmp.get(i,0))