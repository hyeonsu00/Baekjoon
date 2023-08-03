words = input().upper() #upper함수를 이용하여 문자열을 모두 대문자로 변환
unique_words = list(set(words)) #입력받은 문자열에서 set함수를 이용하여 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt) #count 숫자를 리스트에 append
if cnt_list.count(max(cnt_list)) > 1: #count숫자 최대값을 찾고 1보다 크면
    print('?')# ?출력
else:
    max_index = cnt_list.index(max(cnt_list)) #count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])