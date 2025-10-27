#turtle_shape.py

import turtle as t
import random


'''
t.shape("turtle")
t.speed(1000)

#다각형 그리기

n = int(input("몇갂형을 그릴까요? : "))

for i in range(n):
    t.forward(100)
    t.left(360/n)

#2. 다각형 그리기 입력한 각형 -> 삼각형까지 그리기
    
n = int(input("몇갂형을 그릴까요? : "))
t.shape("turtle")
t.speed(0)
for i in range(n,2,-1):
    for j in range(i):
        t.forward(100)
        t.left(360/i)

# 3. 다각형 그리고 색깔 칠하기
color = ["red","green","purple","blue","brown","yellow","teal","gray","pink","orange"]

n = int(input("몇갂형을 그릴까요? : "))
t.shape("turtle")
t.speed(0)
for i in range(n,2,-1):
    t.color(color[i]))
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

# 4. 다각형 그리고 랜덤 색칠하기
color = ["red","green","purple","blue","brown","yellow","teal","gray","pink","orange"]

n = int(input("몇갂형을 그릴까요? : "))
t.shape("turtle")
t.speed(0)
for i in range(n,2,-1):
    # t.color(random.choice(color))
    random.shuffle(color)
    t.color(color[1])
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

#색 중복 없애기

color = ["red","green","purple","blue","brown","yellow","teal","gray","pink","orange"]

n = int(input("몇갂형을 그릴까요? : "))
t.shape("turtle")
t.speed(0)
for i in range(n,2,-1):
    selected_color = random.choice(color)
    print(selected_color)
    t.color(selected_color)
    color.remove(selected_color)
    print(color)
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

'''

# 세가지 색깔이 계속 중복되어서 칠해지도록
# 각형 제한 X

color = ["red","blue"]
count = 0
n = int(input("몇각형을 그릴까요? : "))
t.shape("turtle")
t.speed(0)

for i in range(n,2,-1):
    t.color(color[count])
    count = count +1
    if count == 3:
        count = 0
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()













