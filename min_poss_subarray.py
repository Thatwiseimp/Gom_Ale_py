#Our goal is to find the minimum possible sub array that could be equal or greater than the given expected value

def min_poss_subarray(array,value):
    curr_sum=[]
    start=0
    min_poss=0
    for i in range(len(array)):
        curr_sum.append(array[i])
        while sum(curr_sum)>=value:
            min_poss=len(curr_sum)
            curr_sum.remove(arr[start])
            start+=1
    print(curr_sum)
    print(min_poss)


arr=[2,4,2,5,1]
exp=7
min_poss_subarray(arr,exp)
