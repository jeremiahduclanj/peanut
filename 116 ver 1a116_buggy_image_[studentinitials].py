#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
amountoflegs = 8
legnthoflegs = 70
angleoflegs = 380 / amountoflegs
spider.pensize(5)
n = 0
while (n < amountoflegs):
  spider.goto(0,0)
  spider.setheading(angleoflegs*n)
  spider.forward(legnthoflegs)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()