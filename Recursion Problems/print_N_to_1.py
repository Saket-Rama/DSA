start=int(input())
end=1
def name(s,e):
    if s<e:
        return
    print(s)
    name(s-1,e)
name(start,end)