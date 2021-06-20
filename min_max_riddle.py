# def max_sum(array,k):
#     start=0
#     max_sum=[]
#     curr_sum=[]
#     for end,val in enumerate(array):
#         curr_sum.append(val)
#         if end-start+1==k:
#             max_sum.append(min(curr_sum))
#             curr_sum.remove(array[start])
#             start+=1
#     return max(max_sum)
# def min_max(array):
#     maxima=[]
#     n=len(array)+1
#     for k in range(1,n):
#         maxima.append(max_sum(array,k))
#     return(maxima)


def min_max(arr):
    mini=[]
    n = len(arr)
    for k in range(n+1,1,-1):
        for i in range(len(arr)-1-k):
            window = arr[i:i+k]
            if not mini or arr[i+k]>mini[-1]:
                mini = min(window)
                print(mini)




arr2=[10,20,30,50,10,70,30]
min_max(arr2)
