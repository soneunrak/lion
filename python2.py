from classes import *

print('===================================')
print('회원가입')
print('===================================')

info = SignUp()

username = input('ID: ')
password = info.confirmPw()
name = input('이름: ')
birth_date = info.confirmBD()
email = input('이메일: ')

# user1 인스턴스 생성
user1 = Member(username, password, name, birth_date, email)

print('===================================')
# user1 __str__ 출력
print(user1)
print('===================================')

# user1 info 텍스트 파일로 저장
f = open("user1_info.txt", "w", encoding="UTF-8")
f.write(str(user1.__dict__))
f.write("\n")
f.close()