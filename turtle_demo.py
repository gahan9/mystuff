from turtle import Turtle, Screen
 
#setup(800,600)
wn = Screen() 
wn.title("Handling keypresses!") 
wn.bgcolor("lightblue")
tess = Turtle() 
 
def h1():
  tess.forward(30)
 
def h2():
 tess.left(45)
 
def h3():
   tess.right(45)
 
def h4():
   wn.bye() 
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.listen()
wn.mainloop()
