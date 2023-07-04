t = int(input()) #랜덤의 수를 입력받는다

for x in range(1, t+1): #1부터 t까지
    a,b = map(int, input().split()) #for문 안에서 반복되는 문장을 작성
    print(f'Case #{x}: {a} + {b} = {a+b}') #f-string에 대해서 공부필요!