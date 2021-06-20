import time

def recr_fac(n):
    d={}
    if n==0 or n==1:
        return 1
    else:    
        return n*recr_fac(n-1)
def factorial(n):
    arr=[0]*(n+1)
    arr[0]=1
    for i in range(1,n+1):
        arr[i]+=i*arr[i-1]

    print(arr[n])

n=int(input())
s1=time.time()
factorial(n)
s2=time.time()

print(recr_fac(n))
s4=time.time()
print(s2-s1)
print(s4-s2)
