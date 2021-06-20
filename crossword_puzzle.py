def get_pos_loc(board,word,loc):
    length=len(word)
    #horizontal checking
    for i in range(10):
        for j in range(10-len(word+1)):
            for k in range(len(word)):
                if board[i][j+k] not in ['-', word[k]]:
                    break
            yield(i,j,0)
    #vertical checking
    for i in range(10-len(word)+1):
        for j in range(10):
            for k in range(len(word)):
                if board[i+k][j] not in ['-',word[k]]:
                    break
            yield(i,j,1)


def print_board(board):
    for row in board:
        print(''.join(row))


def move(board,word,loc):
    i,j,axis=loc
    #horizontal checking
    if axis==0:
        for k in range(len(word)):
            board[i][j+k]=word[k]
    #vertical checking
    elif axis==1:
        for k in range(len(word)):
            board[i+k][j]=word[k]


def revert(board,word,loc):
    i,j,axis =loc
    if axis==0:
        for k in range(len(word)):
            board[i][j+k]='-'
    else:
        for k in range(len(word)):
            board[i+k][j]='-'


def solve(board,words):
    if len(words)==0:
        print_board()
        return
    word=words.pop()
    pos_locs=[loc for loc in get_pos_loc(board,word,loc)]

    for loc in pos_locs:
        move(board,word,loc)
        solve(board,words)
        revert(board,word,loc)

for i in range(10):
    board=list(input())

words=list(input().split(','))

solve(board,words)
