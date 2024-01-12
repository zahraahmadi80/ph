import turtle
import random
import time


# return second
def time_second():
    time.localtime()
    s = time.localtime().tm_sec
    return s


# تنظیمات صحنه
window = turtle.Screen()
window.title("لاکپشت و توپ")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# ایجاد لاکپشت
turtle_pen = turtle.Turtle()
turtle_pen.shape("turtle")
turtle_pen.color("green")
turtle_pen.penup()

# ایجاد توپ‌ها
balls = []
num_balls = 1

w = turtle.Turtle()
w.color("black")
w.speed(10)
w.up()
w.goto(-258, 230)
w.down()
w.width(4)
for i in range(4):
    w.forward(515)
    w.right(90)
w.ht()


def create_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(random.randint(360, 380), random.randint(-280, 250))
    balls.append(ball)


# امتیاز
score = 0

# نمایش امتیاز روی صفحه
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("امتیاز: {}".format(score), align="center", font=("Courier", 24, "normal"))


# تابع بررسی برخورد لاکپشت و توپ
def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False


# حرکت لاکپشت
def move_up():
    y = turtle_pen.ycor()
    y += 20
    turtle_pen.sety(y)


def move_down():
    y = turtle_pen.ycor()
    y -= 20
    turtle_pen.sety(y)


def move_left():
    x = turtle_pen.xcor()
    x -= 20
    turtle_pen.setx(x)


def move_right():
    x = turtle_pen.xcor()
    x += 20
    turtle_pen.setx(x)


# اتصال حرکت به کلیدها
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# حلقه اصلی بازی
count = 0
s1 = time_second()
while True:
    tx = int(turtle_pen.xcor())
    ty = int(turtle_pen.ycor())
    if (tx > 248 or tx < -248 or ty > 220 or ty < -278):
        score -= 4
        score_pen.clear()  # پاک کردن
        score_pen.write("امتیاز: {}".format(score), align="center", font=("Courier", 24, "normal"))
        if (tx > 248):
            turtle_pen.setx(turtle_pen.xcor() - 50)
        if (tx < -248):
            turtle_pen.setx(turtle_pen.xcor() + 50)
        if (ty > 220):
            turtle_pen.sety(turtle_pen.ycor() - 50)
        if (ty < -278):
            turtle_pen.sety(turtle_pen.ycor() + 50)
    s2 = time_second()
    if (s1 != s2):
        count += 1
        s1 = s2
    if (count == 4):
        count = 0
        create_ball()
    window.update()
    for ball in balls:
        ball.setx(ball.xcor() - 0.5)  # حرکت توپ به سمت لاکپشت
        # بررسی برخورد لاکپشت و توپ
        if is_collision(turtle_pen, ball):
            ball.goto(random.randint(360, 380), random.randint(-280, 250))
            score += 1  # افزایش امتیاز
            score_pen.clear()  # پاک کردن
            score_pen.write("امتیاز: {}".format(score), align="center", font=("Courier", 24, "normal"))