#입출력문 연습 - print() input()
#주석 - 번역 X # - 한줄 주석
#여러줄 주석 ''' ''' """ """
'''
print("Hello World")
print("원지후")
message = "안녕하세요 저는 인평자동차고등학교 Ai과 1학년 2반 원지후입니다"
print(message*10)

# 변수와 자료형
a = 4
b = 2.5
c = "Hello"
d = 5672
print("a변수에 입력된 값은 ",a,"입니다")
a = 54
print("a변수에 입력된 값은 ",a,"입니다")

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#입력문 - input()
name = input("이름을 입력하세요: ")
#print("입력한 이름은" ,name,"입니다.")
age = input("나이를 입력하세요: ")
print("내 이름은" ,name,"이고, 나이는" ,age,"살입니다.")
'''
# 두 수의 덧셈(키보드로부터 수를 입력받기)
#키보드로부터 입력 받으면 모두 문자로 취급한다.
#형 변환 => 캐스트 연산 cast
a = int(input("첫번째 값을 입력: ")) #캐스트연산 문자->정수
b = int(input("두번째 값을 입력: ")) #str->int
c  = a*b
print(c)








