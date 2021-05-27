def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot=len(array)//2
        left=[]
        right=[]
        for i in range(len(array)):
            if array[i]==array[pivot]:
                pass
            elif array[i]<array[pivot]:
                left.append(array[i])
            
            else:
                right.append(array[i])
            print(left,right,array[pivot],i)
            
    return quick_sort(left)+[array[pivot]]+quick_sort(right)

# a=[1,2,5,7,3,8,31,11,12,21,112,52,32]
# print(quick_sort(a))