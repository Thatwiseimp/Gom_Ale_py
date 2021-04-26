dict={}
li=[]



def allotment(arr,c,n):
    if dict['c']==0:
        print('**No cabs in the pool..Please wait**')
        for i in range(60):
            dict['i']=i

        print(li[0],'added back into the pool')
        dict['c']+=1
        print('cab-',li[0],'allocated to emp-',arr[0],'for slot',arr[1],'(remaining cabs=',dict['c']-1)
        dict['c']-=1
        li.remove(li[0])
    else:
        if int(arr[0]) in dict.keys():
            print('Emp-',arr[0],' is already allocated cab for slot',dict[(int(arr[0]))],' (remaining cabs = ',dict['c'],')')
        else:
            dict['c']-=1
            print('cab-',dict['c']+1,'allocated to emp-',arr[0],'for slot',arr[1],'(remaining cabs=',dict['c'])
            li.append(c)
            
            dict[int(arr[0])]=int(arr[1])
            dict[(int(arr[0]))]=dict['c']+1
            



            
        

def cancel(arr,c,n):
    print('Booking for slot',arr[1], ' cancelled by Emp-',arr[0],'(remaining cabs=',c)
    li.remove(dict[(int(arr[0]))])
    dict['c']+=1
    del dict[(int(arr[0]))]

n=int(input())    
c=int(input())
dict['c']=c

for i in range (9):
    arr=(list(input().split()))
    if arr[2]=='1':
        allotment(arr,n,c)
    elif arr[2]=='-1':
        cancel(arr,n,c)