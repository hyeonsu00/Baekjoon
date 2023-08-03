N = int(input())

for i in range(1,N):
    print(' '*(N-i)+'*'*(2*i-1))

for i in range(N,0,-1):
    print(' '*(N-i)+'*'*(2*i-1))
#range(시작값,끝값,-1)=시작값부터 끝값까지 역순으로 출력