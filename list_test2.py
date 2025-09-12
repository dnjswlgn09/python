# 라스트 변수 - 여러개의 값을 지정
'''
score = []
print(score)
print(type(score))
#soft() 오름차순 정렬
score.sort()
print(score)
h = [5, 4, 9, 2, 7, 3]
# 역순정렬하세요
h.sort()
h.reverse()
print(h)
#h.sort(reverse=true)
fruit = ["바나나","파인애플","키위","망고스틴","카더가든"]
print(fruit)
fruit.remove("파인애플")
print(fruit)
fruit.append("복숭아")
print(fruit)
fruit.pop(0)
print(fruit)
fruit.insert(2, "딸기")
print(fruit)
#리스트 변수 함수 append(), remove(), insert(), pop(), sort(), reverse()
name_list = ["김건영","김의준","김진성","남명진","박한올"]
print(name_list)
name_list[2] = "김하성"
print(name_list)
name_list[4] = "백지율"
print(name_list)
#인덱싱
print(name_list[0:2])
print(name_list[1:4])
print(name_list[0:5:2])
print(name_list[1:4:2])
print(len(name_list))
print("남명진"in name_list)
h = [5, 4, 9, 2, 7, 3]
print(7 in h)
print(8 in h)
print(9 not in h)
'''
import random
#random() 변수발생
x = random.random() #0-1 사이의 난수 값
print(x)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)
y = random.choice(x)
print(y)
random.shuffle(x)
print(x)
z = random.sample(x,2)
print(z)
