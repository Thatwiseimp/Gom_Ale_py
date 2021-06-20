def maxSubsetSum(arr):
    store=[]
    max_sum=[]
    _sum=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr),1):
            store.append([arr[i],arr[j]])


    print(store)

if __name__ == '__main__':

    arr=[-2,1,3,-4,5]
    print(maxSubsetSum(arr))