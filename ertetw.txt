#group members: George, Jeramiah, Kunsh, Yidam
import turtle as trtl
painter = trtl.Turtle()

#ask user for the equation, slope, and y-intercept (POSITIVE NUMBERS ONLY)
#eq = int(input("Input Equation in y = mx + b form: "))
#slope = int(input("What is the slope?: "))
#yint = int(input("What is the y-intercept?: "))

#graph (the y and x axis)
def make_graph():
    painter.speed(0)
    painter.setposition(0,0)
    
    for i in range (4):
        painter.forward (400)
        painter.backward(400)
        painter.right(90)
    
    painter.setposition(-400,0)
    for i in range (80):
        painter.forward(10)						
        painter.right(90)
        painter.backward(5)
        painter.forward(5)
        painter.left(90)
    
    painter.setposition()
    for i in range (80):

        
    

make_graph()





  

wn = trtl.Screen()
wn.mainloop()