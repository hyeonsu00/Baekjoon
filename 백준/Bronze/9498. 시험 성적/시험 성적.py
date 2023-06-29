score = int(input()) #점수를 정수로 입력받음

if score >= 90 :  # 90점 이상일때
    print('A')  #A학점
elif score >= 80 : #80점 이상일때
    print('B')  # B학점
elif score >= 70 :  # 70점 이상일때
    print('C')  # C학점
elif score >= 60 :  # 60점 이상일때
    print('D')  # D학점
else:
    print('F') #나머지 점수 F학점
    
    #삼항 연산자로 출력가능하지만 조건이 많아서 한눈에 보기 어렵다