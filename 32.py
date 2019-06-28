def A(a,d):
    b=[]
    for i in range(0,len(a)):
        if i%2!=0:
            b.append(a[i])
    if len(b)!=1:
        A(b,d)
    else:
        print(d.index(b[0]))
ax=int(input())
a=list(map(int,input().split()))
d=a
A(a,d)
