piece = [1,1,2,2,2,8] #필요한 각각의 피스 수를 하나의 리스트로 선언
input = list(map(int, input().split())) #킹,퀸,룩,나이트,폰을 리스트형태로 차례로 입력받음
for i in range(len(piece)): #몇개의 피스를 더하거나 빼야되는지 출력
    print(piece[i] - input[i], end=' ') #요구 피스 수 - 갖고있는 피스 수 = 필요한 피스 수