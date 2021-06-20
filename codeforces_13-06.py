# Today we will be playing a red and white colouring game (no, this is not the Russian Civil War; these are just the colours of the Canadian flag).
#
# You are given an 𝑛×𝑚 grid of "R", "W", and "." characters. "R" is red, "W" is white and "." is blank. The neighbours of a cell are those that share an edge with it (those that only share a corner do not count).
#
# Your job is to colour the blank cells red or white so that every red cell only has white neighbours (and no red ones) and every white cell only has red neighbours (and no white ones). You are not allowed to recolour already coloured cells.
#
# Input
# The first line contains 𝑡 (1≤𝑡≤100), the number of test cases.
#
# In each test case, the first line will contain 𝑛 (1≤𝑛≤50) and 𝑚 (1≤𝑚≤50), the height and width of the grid respectively.
#
# The next 𝑛 lines will contain the grid. Each character of the grid is either 'R', 'W', or '.'.
#
# Output
# For each test case, output "YES" if there is a valid grid or "NO" if there is not.
#
# If there is, output the grid on the next 𝑛 lines. If there are multiple answers, print any.
#
# In the output, the "YES"s and "NO"s are case-insensitive, meaning that outputs such as "yEs" and "nO" are valid. However, the grid is case-sensitive.
#
# Example
# inputCopy
# 3
# 4 6
# .R....
# ......
# ......
# .W....
# 4 4
# .R.W
# ....
# ....
# ....
# 5 1
# R
# W
# R
# W
# R
# outputCopy
# YES
# WRWRWR
# RWRWRW
# WRWRWR
# RWRWRW
# NO
# YES
# R
# W
# R
# W
# R


def colourize(arr,x,y):
    poss1=[['R','W']*(y//2),['W','R']*(y//2)]*(x//2)
    poss2=[['W','R']*(y//2),['R','W']*(y//2)]*(x//2)

    for i in range(x):
        for j in range(y):
            if arr[y][x]=='R' and poss1[y][x]=='R':
                print('poss1 matches')

            elif arr[y][x]=='W' and poss1[y][x]=='W':
                print('poss2 matches')

if __name__=='__main__':
    board=[
        ['.','R','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','W','.','.','.','.'],
        ]
    # ic(solve(board))
    colourize(board,4,6)
    print(board)
