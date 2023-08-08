password=1234
masterpw=0000
num=int(input("비밀번호를 입력해주세요:"))
if password==num:
    print('문이 열렸습니다')
elif masterpw==num:
    print('오셨습니까')
else:
    print('누구세용?')
