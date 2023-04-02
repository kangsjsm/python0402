# 함수로 태극문양 그리기

import turtle as t
t.bgcolor('black')
t.speed(0)

for x in range(500):
    if x % 3 == 0:
        col = 'red'
    elif x % 3 == 1:
        col = 'blue'
    else :
        col = 'yellow'
    
    t.color(col)
    t.forward(x * 2)
    t.left(119)
