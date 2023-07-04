x = int(input()) #영수증에 적힌 총 금액 X를 입력 받는다.
sum = 0

for _ in range(int(input())):   #구매한 물건의 종류의 수 N만큼 반복, a와 개수 b를 입력받음.
    a,b = map(int, input().split())
    sum += a*b
    
print("Yes") if sum == x else print("No")