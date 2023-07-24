while True: 
    try: #try,except 구문을 통해 입력값이 계속 들어오면 그대로 출력해줌
        print(input())
    except EOFError: #EOF(End Of File)상태라면 break를 걸어줌
        break