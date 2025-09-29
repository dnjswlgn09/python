#for_test2.py

#if문 복습
'''
k = int(input('구분 : 1. 주간 2. 야간? : '))
m = int(input('대상: 1. 대인 2. 소인? : '))

if k==1: #주간
    if m==1:
        pay = 50000
    else:
        pay = 40000
else:
   if m==1:
      pay = 30000
   else:
      pay = 20000

print(f"당신의 입장료는 {pay}원 입니다.")

# for 반복문
#2. 리스트 변수를 이용한 반복문
fruit = ['mango', 'apple', 'orange', 'kiwi', 'banana']
count = 0
#print(fruit[2])

for i in fruit:
    count +=1 #count = count +1
    print(f'{count}. {i}')


n = [0,1,2,3,4]

for i in n:
    print(i+1,". 안녕하세요")


food = ("인절미 빙수", "딸기 빙수", "멜론 빙수", "망고 빙수", "수박 빙수", "치즈 빙수")

print(type(food))

for f in food:
    print(f)



number = [273,103,5,32,65,9,72,880,99,58]

for i in number:
    if i % 2 ==0:
        print(f"{i}은 짝수입니다") #print(n, "은 짝수입니다")
    else:
        print(f"{i}은 홀수입니다")

number = [273,103,5,32,65,9,72,880,99,58]

#273은 3자리수입니다. #len str

for i in number:
    print(f"{i}은 {len(str(i))}자리수 입니다.")

'''

score_list = [98,58,65,78,44]
count = 0
total = 0
average = 0
for i in score_list:
    count += 1
    if i >=60:
        print(f"{count}번 학생은 {i}점으로 합격입니다.")
        total += i
        average += 1
    else:
        print(f"{count}번 학생은 {i}점으로 불합격입니다.")

print(f"합격한 친구들의 총점은 {total}입니다.")
print(f"합격한 친구들의 평균은 {round(total/average,2)}입니다.")

# 합격한 친구들의 평균 점수를 구하세요

















