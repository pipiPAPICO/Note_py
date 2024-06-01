import turtle as t
t.shape("turtle")
t.home()
t.speed(10.5)
size = 250 # size는 원의 지름 (즉, 비율 1)
alpha = 38.197

# 테두리
def rectangle(size):
    t.penup()
    t.forward(size*3/2)
    t.pendown()
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size*3)
    t.right(90)
    t.forward(size*2)
    t.right(90)
    t.forward(size*3)
    t.right(90)
    t.forward(size)
    t.penup()
    t.home()
    t.pendown()
    
# 태극 문양
def drawCircle(size):
    t.pencolor("red")
    t.fillcolor("red")
    t.right(38.197)
    t.begin_fill()
    t.forward(size/2)
    t.left(90)
    t.circle(size/2,180)
    t.end_fill()
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(size/2, 180)
    t.circle(size/4, 180)
    t.right(90)
    t.forward(size/2)
    t.end_fill()
    t.pencolor("red")
    t.fillcolor("red")
    t.left(90)
    t.begin_fill()
    t.circle(size/4)
    t.end_fill()
    
# 검은색 박스(건곤감리를 그리기 위한 기초 공사)
def drawBlackBox(size,angle):
    t.pencolor("black")
    t.fillcolor("black")
    t.penup()
    t.home()
    t.setheading(angle)
    t.forward(size/2+size/4)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.forward(size/4)
    t.right(90)
    t.forward(size/3)
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/3)
    t.right(90)
    t.forward(size/4)
    t.end_fill()

# 검은색 박스를 세 줄로 나누는 함수
def remove_LongLine(size):
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.forward(size/4)
    t.right(90)
    t.pendown()
    t.forward(size*3/24)
    t.begin_fill()
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/24)
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/24)
    t.end_fill()
    t.forward(size*3/24)
    t.begin_fill()
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/24)
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/24)
    t.end_fill()

# 건곤감리의 긴 한 줄을 두 개로 나누는 함수
def remove_ShortLine(size, angle, location):
    t.penup()
    t.home()
    t.setheading(angle)
    t.forward(size/2 + location) # location : 곤, 감, 리에서 각각 두 개로 나눠야하는 긴 줄.
    t.pendown()
    t.begin_fill()
    t.right(90)
    t.forward(size/48)
    t.left(90)
    t.forward(size/12)
    t.left(90)
    t.forward(size/24)
    t.left(90)
    t.forward(size/12)
    t.left(90)
    t.forward(size/48)
    t.end_fill()


# 건, 곤, 감, 리를 각각 그리는 함수들
def drawGun(size, angle):
    alpha = 180 - angle
    drawBlackBox(size, alpha)
    remove_LongLine(size)
    
def drawGon(size, angle):
    alpha = -angle
    drawBlackBox(size, alpha)
    remove_LongLine(size)
    remove_ShortLine(size, alpha, size/4)
    remove_ShortLine(size, alpha, size/4 + size*3/24)
    remove_ShortLine(size, alpha, size/4 + size*6/24)
    
def drawGam(size, angle):
    alpha = angle
    drawBlackBox(size, alpha)
    remove_LongLine(size)
    remove_ShortLine(size, alpha, size/4)
    remove_ShortLine(size, alpha, size/4 + size*6/24)
    
def drawLi(size, angle):
    alpha = 180 + angle
    drawBlackBox(size, alpha)
    remove_LongLine(size)
    remove_ShortLine(size, alpha, size/4 + size*3/24)
    
                     
# 건곤감리를 모두 그리는 함수
def GunGonGamLi(size, angle):
    drawGun(size, angle)
    drawGon(size, angle)
    drawGam(size, angle)
    drawLi(size, angle)
    

# 태극기를 그리는 함수
def Taegeukgi(size):
    rectangle(size)
    drawCircle(size)
    GunGonGamLi(size, alpha)
    t.hideturtle()

Taegeukgi(size)
