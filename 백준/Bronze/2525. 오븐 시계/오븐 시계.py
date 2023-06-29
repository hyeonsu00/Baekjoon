h, m = map(int,input().split())
c = int(input())

h += c // 60
m += c % 60

if (m >= 60): #분(minute)은 60을 초과하면 안돼서 빼줌
    m -= 60
    h += 1
    
if(h >= 24): #시(hour)은 24를 초과하면 안돼서 빼줌
    h -= 24
print(h,m)