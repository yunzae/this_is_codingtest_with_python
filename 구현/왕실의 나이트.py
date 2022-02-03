####  내코드
import sys
myinput=sys.stdin.readline()
board_x= {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
x=board_x[myinput[0]]
y=int(myinput[1])
move_first=[2,-2]
move_second=[1,-1]
result=0
for i in move_first:
    for j in move_second:
        if (x+i>0 and x+i<9 and y+j>0 and y+j<9):
            result += 1
        if (y+i>0 and y+i<9 and x+j>0 and x+j<9):
            result += 1
print(result)

### 예시코드
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]