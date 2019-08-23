# demo11.py

# 绘制七段数码管并显示时间(本地)
# I:数字形式的字符串(日期)
# P:根据数字绘制数码管
# O：绘制当前日期形式的七段数码管

import turtle, datetime


def DrawGap():
    # 数码管间间隔绘制
    turtle.penup()
    turtle.fd(5)


def DrawLine(draw):
    # 绘制单段数码管
    DrawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    DrawGap()
    turtle.right(90)


def DrawDight(digit):
    # 根据数字绘制七段数码管
    # 先绘制下半段
    DrawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else DrawLine(False)
    DrawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else DrawLine(False)
    DrawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else DrawLine(False)
    DrawLine(True) if digit in [0, 2, 6, 8] else DrawLine(False)
    # 再绘制上半段
    turtle.left(90)
    DrawLine(True) if digit in [0, 4, 5, 6, 8, 9] else DrawLine(False)
    DrawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else DrawLine(False)
    DrawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else DrawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def DrawDate(date):
    # 获得需要输出的数字
    turtle.pencolor("red")
    for i in date:
        if i == '-':  # '-'替换 '年'
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':  # '=' 替换 '月'
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':  # '+'替换 '日'
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            DrawDight(eval(i))  # eval传递值，而不是字符串


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)

    # DrawDate('123456')
    DrawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))  # 绘制时间段，定义格式
    turtle.hideturtle()


main()

