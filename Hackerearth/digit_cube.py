# Digit cube
# https://www.hackerearth.com/problem/algorithm/digit-cube-1cc1e002/?source=list_view
def cube(n,k):
    sum=0
    for i in range(int(k)):
        for i in str(n):
            sum+=int(i)
            
        cubic=int(sum)**3
        n=cubic
        sum=0
        

    return cubic
tests=int(input())
for i in range(tests):
    n,k= input().split()
    print(cube(n,k))
