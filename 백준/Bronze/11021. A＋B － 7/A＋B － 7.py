t = int(input())

for i in range(1, t+1): #1부터 t까지)
    a,b = map(int, input().split())
    print(f'Case #{i}: {a+b}')
    #f-string 사용 문자열은 그대로 놔두고 출력되는 숫자만 변경하고자할때사용