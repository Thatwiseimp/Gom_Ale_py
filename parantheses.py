x=input('')

l1=['{','(','[']
l2=['}',')',']']

li=[]
for i in x:
    if i in l1:
        li.append(i)
    elif i in l2:
        temp=l2.index(i)
        if len(li)>0 and l1[temp]==li[len(li)-1]:
            li.pop()
        else:
            return print('unbalanced')
if len(li)==0:
    print('Balanced')
else:
    print('unbalanced')



    
    
