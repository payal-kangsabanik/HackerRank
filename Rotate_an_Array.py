n,k=map(int,input().split())
arr=list(map(int,input().split()))
if k > n:
    k=k%n
for i in range(k):
    arr=[arr[-1]]+arr[:-1]
print(*arr)