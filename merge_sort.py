def merge__sort(a,b,arr):
    i=j=k=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1
         

def merge_sort(arr):
    if len(arr)<=1:
        return 
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge__sort(left,right,arr)







arr=[2,12,5,17,52,13,27,1,3,81]
merge_sort(arr)
print(arr)