wt=[]
val=[]
fxd=11
max=0
for i in range(4):
    arr=list(map(int,input().split()))
    wt.append(arr[0])
    val.append(arr[1])
for i in range(len(wt)):
    if (wt[i]<fxd) and (fxd-wt[i] in wt):
        x=wt.index((fxd-wt[i]))
        if (wt[x]+wt[i])>max:
            max=wt[x]+wt[i]
        
    elif(wt[i]<fxd) and  (fxd-wt[i] not in wt):
        if (wt[i])>max:
            max=wt[i]

print(max)
