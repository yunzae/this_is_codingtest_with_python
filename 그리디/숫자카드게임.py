###내코드
import sys
n,m = map(int,sys.stdin.readline().split(" "))
result=0
for i in range(n):
    mylist = list(map(int,sys.stdin.readline().split(" ")))
    mylist.sort()
    if result<mylist[0]:
        result=mylist[0]
print(result)
"""

"""
n, m = map(int,input().split())

result=0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)

###예시코드
n,m = map(int,input().split())

result =0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result,min_value)
print(result)
