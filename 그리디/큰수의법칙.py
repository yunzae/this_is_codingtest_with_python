#내코드
import sys
n,m,k = map(int,sys.stdin.readline().rstrip().split(" "))
mylist = []
temp= sys.stdin.readline().rstrip().split(" ")
for i in range(n):
    mylist.append(temp[i])
mylist.sort()
result = (m/(k+1))*(int(mylist[-1])*k+int(mylist[-2]))+(m%(k+1))*int(mylist[-1])
print(int(result))

#예시코드
import sys
n,m,k = map(int,sys.stdin.readline().split(" "))
data = list(map(int,input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) *k
count +=m%(k+1)

result = 0
result += (count) * first
result += (m-count) *second

print(result)
