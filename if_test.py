#제어문-조건문(선택문)

'''
#예제1 홀짝 판별 프로그랩

num = int(input("자연수 입력: "))
#1. 단일 선택문(단일 조건문)"짝수면 *출력
if num % 2 == 0: #짝수라면
    print("*")
    print(num)

#2. 이중 선택문(이중 조건문) :짝수면 - 짝수입니다 홀수면 - 홀수입니다
if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
    
#예제 2 나이판별

# 나이가 17살 이상이면 "다 컸네" 그렇지 않으면 "넌 아직 어려" 출력
age = int(input("나이 입력: "))

if age >= 17:
    print("다 컸네")
else:
    print("넌 아직 어려")

#예제 3 점수입력받아 80점 이상이면 합격 그렇지 않으면 불합갹 출력
score = int(input("점수 입력: "))

if score >= 80:
    print("합격")
else:
    print("불합격")

# 다중 선택문 if~elif~else
3 나아 8미만이면 유아 19살 이하 학생 그외에는 성인 출력

if age = age = int(input("나이 입력: "))
if age < 8:
    print("당신은 유아입니다")
elif age >= 8 an age <=19: #7<age<=19
    print("당신은 학생입니다")
else:
    print("당신은 성인입니다")

# 요일 입력 받고 일요일이면  "게임 열판하기" 출력
today = input("요일 입력: ")

if today == "일요일":
    print("게임 열판하기")
elif today == "토요일":
    print("밤새서 게임 하기")
else:
    print("물 한잔 하기")
print("공부 시작")

#리조트에 객실당 4명의 손님까지 무료 입장입니다.
total = int(input("입장 인원 입력: "))

if total <= 4:
    print("추가비용이 없습니다.")
elif total ==5:
    print("추가비용은 1만원입니다.")
elif total ==6:
    print("추가비용은 2만원입니다.")
elif total ==7:
    print("추가비용은 3만원입니다.")
elif total ==8:
    print("추가비용은 4만원입니다.")
elif total > 8:
    print("입장인원은 최대 8명입니다.")
else:
    print("추가비용 1인당 1만원 입니다.")
'''

temp = int(input("온도입력: "))

if temp >= 40:
    print("고열입니다. 병원으로 뛰어가세요")
elif temp >= 38:
    print("병원에 가세요")
elif temp >= 37:
    print("하교에 가서 보건선생님을 만나요")
else:
    print("정상입니다 당장 학교로 가세요")
