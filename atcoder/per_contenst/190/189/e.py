import sys
input=sys.stdin.readline
N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
M=int(input())
Memos = [[[1,0,0],[0,1,0],[0,0,1]]]

def calc1(is_clockwise):
    if is_clockwise:
        t = [
            [0,1,0],
            [-1,0,0],
            [0,0,1]
        ]
    else:
        t = [
            [0,-1,0],
            [1,0,0],
            [0,0,1]
        ]
    pre = Memos[-1]
    tmp = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp[i][j]+=t[i][k]*pre[k][j]
    Memos.append(tmp)

def calc2(p,is_x):
    if is_x:
        t = [
            [-1,0,2*p],
            [0,1,0],
            [0,0,1]
        ]
    else:
        t = [
            [1,0,0],
            [0,-1,2*p],
            [0,0,1]
        ]
    pre = Memos[-1]
    tmp = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp[i][j]+=t[i][k]*pre[k][j]
    Memos.append(tmp)



for i in range(M):
    op=input().split()
    if op[0] == '1':
        calc1(True)
    elif op[0] == '2':
        calc1(False)
    elif op[0] == '3':
        calc2(int(op[1]), True)
    elif op[0] == '4':
        calc2(int(op[1]), False)

Q=int(input())
for _ in range(Q):
    a,b=list(map(int,input().split()))
    b-=1
    x,y=XY[b]
    memo = Memos[a]
    x_sum = (memo[0][0]*x + memo[0][1]*y + memo[0][2])
    y_sum = (memo[1][0]*x + memo[1][1]*y + memo[1][2])
    print(x_sum,y_sum)