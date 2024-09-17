time.sleep(0.1)
  canvas = turtle.getcanvas()
  x = canvas.winfo_pointerx() - turtle.window_width() / 2 + 10
  y = -canvas.winfo_pointery() + turtle.window_height() / 2 + 15
  turtle.setheading(turtle.towards(x, y))
  turtle.forward(15)