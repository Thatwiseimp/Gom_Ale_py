

def find_next(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j

    return None,None

def possible(puzzle,r,c,num):
    if num in puzzle[r]:
        return False
    cols=[puzzle[i][c]for i in range(9)]
    if num in cols:
        return False
    x0=r//3*3
    y0=c//3*3
    for i in range(x0,x0+3):
        for j in range(y0,y0+3):
            if num==puzzle[i][j]:
                return False
    return True


def solve(grid):
    r,c=find_next(grid)
    if r is None:
        return True
    for num in range(1,10):
        if possible(grid,r,c,num):

            grid[r][c]=num
            if solve(grid):
                return True
        grid[r][c]=0
    return False
if __name__=='__main__':
    board=[
    [4,0,0,0,0,5,0,9,0],
    [0,2,0,0,9,0,0,3,0],
    [1,0,0,6,0,0,4,0,0],
    [0,0,0,2,0,1,0,0,3],
    [0,4,0,0,0,0,0,5,0],
    [2,0,0,7,0,3,0,0,0],
    [0,0,2,0,0,8,0,0,9],
    [0,6,0,0,2,0,0,1,0],
    [0,7,0,9,0,0,0,0,4]
    ]
    # ic(solve(board))
    print(solve(board))
    print(board)
