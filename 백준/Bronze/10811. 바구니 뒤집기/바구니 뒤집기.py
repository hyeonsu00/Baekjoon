N,M = map(int, input().split())  
l = [i+1 for i in range(N)]

for _ in range(M):
    i,j = map(int, input().split())
    l = l[:i-1] + l[i-1:j][::-1] + l[j:] #[::-1] -> 역순으로 표현하겠다는것
    
print(*l)