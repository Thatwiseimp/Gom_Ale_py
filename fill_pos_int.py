def find_zeroes(array):
    store=[]
    for i in range(len(array)):
        if array[i]==0:
            store.append(i)
    return store

def position_int(array,zer,affinity):
    count=0
    if zer and affinity>0:
        for i in zer:
            array[i]=1
            affinity-=1
            zer.pop(0)
    print(zer,array)
    return zer,array

def check_for_more(array1,array2,zer1,zer2):

    if zer1:
        for i in zer1:
            array1[i]=1
            if zer2:
                array2[zer2[0]]+=1
            else:
                print('impossible')
    else:
        for i in zer2:
            array2[i]=1
            if zer1:
                array1[zer1[0]] += 1
            else:
                print('impossible')
    return array1,array2
def fill_pos_int(array1,array2):
    sum1=sum(array1)
    sum2=sum(array2)
    zer1=find_zeroes(array1)
    zer2=find_zeroes(array2)
    diff = (sum1 - sum2)
    affinity1=0-diff
    affinity2=1-affinity1
    position_int(array1,zer1,affinity1)
    position_int(array2,zer2,affinity2)
    check_for_more(array1,array2,zer1,zer2)


    # print(array1,array2)




arr1=[0,0,0]
arr2=[1,1]
fill_pos_int(arr1,arr2)