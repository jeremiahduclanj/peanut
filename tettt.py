#group members: George, Jeramiah, Kunsh, Yidam
import turtle as trtl
painter = trtl.Turtle()

#ask user for the equation, slope, and y-intercept (POSITIVE NUMBERS ONLY)
eq = int(input("Input Equation in y = mx + b form: "))
slope = int(input("What is the slope?: "))
yint = int(input("What is the y-intercept?: "))




def make_graph ():
    painter.speed(0)
    Painter.setposition(-200,-200)
    Painter.pensize(5)
    painter.forward(400)
    Painter.penup()
    Painter.setposition(-200,-200)
    Painter.left(90)
    Painter.pendown()
    Painter.forward(400)
    Painter.setposition(-200,-200)
    

make_graph()
wn = trtl.Screen()
wn.mainloop()