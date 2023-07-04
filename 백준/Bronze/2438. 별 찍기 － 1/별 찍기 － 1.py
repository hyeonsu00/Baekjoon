n = int(input())

for i in range(1, n+1): #1부터 n까지
    print('*'* i)
    
#comprehension 코드
#[print('*'*i) for i in range(1, int(input())+1)]