#turtle_pattern.py

from turtle import *  # turtle 모듈을 가져옵니다. turtle은 그래픽을 그릴 수 있는 라이브러리로, 화면에 도형을 그리거나 색을 칠할 수 있습니다.
import turtle
'''
color('green', 'orange')  # 펜 색을 'red'로, 채우기 색을 'yellow'로 설정합니다.
# 첫 번째 매개변수는 펜 색상, 두 번째는 도형을 채울 색입니다.

begin_fill()  # 도형을 그리기 시작하면서 색을 채우기 시작합니다. 그려지는 도형 안쪽은 'yellow' 색으로 채워집니다.

while True:  # 무한 루프를 시작합니다. 이 루프는 조건이 만족될 때까지 계속 실행됩니다.
    forward(200)  # 현재 방향으로 200 픽셀만큼 직선을 그립니다.
    left(170)  # 그 후, 왼쪽으로 170도 회전합니다. 이 각도는 별 모양을 형성하는데 필요한 중요한 각도입니다.

    if abs(pos()) < 1:  # 현재 위치(pos())와 원점(0, 0) 사이의 거리가 1 픽셀 미만인지를 확인합니다.
        # pos()는 터틀의 현재 좌표를 반환하며, abs()는 그 좌표의 절댓값을 구합니다.
        # 원점과의 거리가 거의 0에 가까운 경우, 즉 시작점 근처로 돌아왔을 때 루프를 종료합니다.
        break  # 루프를 종료하여 더 이상 그리지 않고 도형을 완성합니다.

end_fill()  # 도형을 다 그린 후, 채우기를 마칩니다. 이 시점에서 도형의 안쪽이 'yellow'로 채워집니다.

done()  # 그래픽을 종료하고, 창을 닫지 않고 계속 화면에 유지합니다.
'''
bgcolor("black")
speed(0)
color('white','white')

begin_fill()

while True:
    forward(50)
    left(10)
    circle(200,10)
    if abs(pos()) < 1:
        break

end_fill()
done()





















