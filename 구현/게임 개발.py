

import sys
direction=[(0,-1),(1,0),(0,1),(-1,0)] #북,동,남,서
mymap = []
n,m=map(int,sys.stdin.readline().split())
visit = [[True]*n for _ in range(m)]
x, y, start_direction = map(int,sys.stdin.readline().split())
for i in range(n):
    mymap.append(list(map(int,sys.stdin.readline().split())))
result=0
def move(x,y,d):
    visit[x][y]=False
    mymap[x][y]= 2
    global result
    result +=1
    for i in range(4):
        if mymap[x+direction[(d-1+4)%4][0]][y+direction[(d-1+4)%4][1]]==0 and visit[x+direction[(d-1+4)%4][0]][y+direction[(d-1+4)%4][1]]==True:
            x=x+direction[(d-1+4)%4][0]
            y = y + direction[(d - 1 + 4) % 4][1]
            d= (d - 1 + 4) % 4
            move(x,y,d)
        else:
            d=(d-1+4)%4


move(x,y,start_direction)

print(result)

