import turtle as trtl

t = trtl.Turtle()

my_turtles = []


turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t.penup()
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)


startx = 2
starty = 2




for t in my_turtles:
  t.circle(90)
  t.right(100)     
  t.forward(90)


wn = trtl.Screen()
wn.mainloop()