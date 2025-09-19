#if_test.py
#반올림 round() 포매팅
'''
print(round(5.5795,2))#5.58
print(round(5.5295,1))#5.6
print(round(5.5795,0))#6.0
print(round(5.5795,-1))#10.0
print(round(5.5795))#6  
a = round(5.5295)
b = round(5.5295,0)
print(type(a))  #int
print(type(b)) #float

# 포매팅
print("{:.1f}".format(3.5289))
print("{:.0f}".format(3.5289))
print("{:.3f}".format(3.5289)) #3.529

print("{0}과 {0}".format(3.5555, 3.7777)) #인덱스
print("{0}과 {1}".format(3.5555, 3.7777))
print("{0:.2f}과 {1:.1f}".format(3.5555, 3.7777))
print("{1:.1f}과 {0:.2f}".format(3.5555, 3.7777))
a = "{:.1f}".format(3.5289)
print(type(a))

a = 5
b= 8 
if a>=b:
    print(a+b)
else:
    print(a*b)


# # 중국집 메뉴선택 조건

money = int(input("가지고 있는 돈은 얼마인가요? : "))

if money >= 20000:
    print("탕수육 먹어요")
elif money >= 10000:
    print("쟁반짜장 먹자!")
elif money >= 8000:
    print("해물짬뽕 어때?")
elif money >= 6000:
    print("짜장면 먹지 뭐!")
else:
    print("단무지나 먹어야겠다")
'''
scores = [85, 92, 78, 95, 88]

print("입력된 점수 : ",scores)
print("전체 학생 수 : ",len(scores),"명")
if len(scores)>0:
    max_score = max(scores)
    min_score = min(scores)
    tot_score = sum(scores)
    avg_score = sum(scores)/len(scores)
    print("최고 점수 : ",max_score,"점")
    print("최저 점수 : ",min_score,"점")
    print("총합 점수 : ", tot_score,"점")
    print("평균 점수 : ","{:.2f}".format(avg_score),"점")
else:
    print("입력된 점수가 없습니다.")




















