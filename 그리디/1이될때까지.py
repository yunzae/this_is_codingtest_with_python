import sys
n, k = map(int,sys.stdin.readline().split(" "))
result=0
while (n!=1):
    if(n%k==0 and n>k):
        n/=k

    else:
        n-=1
    result+=1
print(result)


####################

n,k = map(int,input().split())
result=0

#N이 K이상이라면 K로 계속 나누기
while n>=k:
    #N K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n%k !=0:
        n-=1
        result+=1
    #k로 나누기
    n//=k
    result+=1

while n>1:
    n-=1
    result+=1

print(result)

####################
n, k =map(int,input().split())
result = 0
while True:
    #(N==k로나누어떨어지는수)가 될때까지 1씩빼기
    #나였으면 %이용해서 구현할듯
    target = (n//k)*k
    result += (n-target)
    n=target
    #N이K보다 작을때(더이상나눌수없을떄)반복문탈출
    if n<k:
        break
    #k로 나누기
    result+=1
    n//=k
#마지막으로 남은수에 대하여 1씩 빼기
result +=(n-1)
print(result)