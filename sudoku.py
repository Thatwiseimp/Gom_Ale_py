def possible(x,y,num):
    for i in range(0,9):
        if grid[i][x]==n:
            return false
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    x0=x//3*3
    y0=y//3*3
    for i in range(0,3):
        for i in range(0,3):
            if grid[[y0+i][x0+i]==n:
                return False
            return True

def solve():
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for num in range(1,10):
                    if possible(x,y,num):
                        grid[y][x]=num
                        solve()
                        grid[y][x]=0
                    return
    print(np.matrix(grid))



puzz=[]
for i in range(9):
    puzz.append(list(input().split()))
print(puzz)
