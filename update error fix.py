import turtle

wn = turtle.Screen()
wn.tracer(0)

player = turtle.Turtle()

while True: # You can use other stuff other than True
    try:
        wn.update()
        player.right(30)
    except:
        break