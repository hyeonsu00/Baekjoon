students = [i for i in range(1,31)] #1~30까지의 수를 students 리스트에 저장

for _ in range(28): #과제를 제출한 28명의 학생을 입력받아 applied에 저장
    applied = int(input())
    students.remove(applied) #remove함수를 이용하여 num에 해당하는 수를 삭제

print(min(students)) #남은 2개의 값중에서 min값과 max값 출력
print(max(students))