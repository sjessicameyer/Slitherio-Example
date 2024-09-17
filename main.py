
#while loops - run while a certain condition is true (indefinite)
"""i = 2
while i<=10:
  print(i)
  i += 2"""

#for loops
"""for i in range(20, 30, 3):
  print(i)"""
"""students = ["Luc", "Lucas", "Terry 'the cool one'", "Cason 'plays zelda tears of the kingdom'", "Jamie 'that kid'"]
for s in students:
  if 'o' in s:
    print(s)"""

#APPLY to turtle
import turtle, time, random

sc = turtle.Screen()
sc.tracer(0)
sc.setup(1.0,1.0)

timmy = turtle.Turtle()
timmy.shape("circle")
timmy.turtlesize(2.5, 2.0)
timmy.speed(0)
timmy.up()

food = turtle.Turtle()
food.shape("circle")
food.color("#cbac00")
food.up()
food.hideturtle()

foodcounter = 0

timmyfoodlist = []
def timmyfood():
  global timmyfoodlist
  newfood = food.clone()
  newfood.showturtle()
  timmyfoodlist.append(newfood)
  x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
  y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
  newfood.goto(x, y)
  

with open("colors.txt") as f:
  colors = f.readlines()

canvas = turtle.getcanvas()
timmybody = []
while True:
  timmyfood()
  colors.reverse()
  for c in colors:
    timmy.color(c.strip())
    time.sleep(0.01)

    #get mouse location
    x = canvas.winfo_pointerx() - turtle.window_width() / 2 + 10
    y = -canvas.winfo_pointery() + turtle.window_height() / 2 + 15
    timmy.setheading(timmy.towards(x,y))
    timmy.forward(3)
    #timmy.stamp()
    sc.update()

    flag = False #indicate if we've spawned a body part
    for f in timmyfoodlist:
      if timmy.distance(f) < 20:
        f.hideturtle()
        timmyfoodlist.remove(f)
        foodcounter += 1
        newbody = timmy.clone()
        timmybody.append(newbody)
        flag = True
    if flag == False and len(timmybody) > 0:
      timmybody[0].goto(timmy.xcor(), timmy.ycor())
      timmybody[0].color(c.strip())
      timmybody[0].setheading(timmy.towards(x,y))
      timmybody.append(timmybody.pop(0))
    for b in timmybody:
      b.forward(0)
