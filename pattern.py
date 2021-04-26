def pyr(num):
    m=2*num+2
    for i in range(num):
        for j in range(m):
            print(end=" ")
        for j in range(i+1):
            print("*" ,end=' ')
        print('\n')
num=int(input())
pyr(num)