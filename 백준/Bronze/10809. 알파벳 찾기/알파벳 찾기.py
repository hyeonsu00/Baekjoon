word = input()
alphabet = list(range(97,123)) #아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)))
    
#chr 함수는 아스키코드에 해당하는 숫자를 문자열로 변환시키는 함수