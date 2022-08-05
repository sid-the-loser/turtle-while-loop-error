import turtle
import tkinter

window = turtle.Screen() 

pen = turtle.Turtle() 

while True:
    try:
        try: 
            window.update()
            pen.goto(0, 0)
            pen.forward(30)
            pen.right(30)
            
        except turtle.Terminator:
            print("Terminator error!") # optional
            break
    except tkinter.TclError:
        print("TclError error!") # optional
        break
    
"""

There are two common types of error that turtle
makes when you close it's window while running a
while loop. This error is caused due to an un-
avoidable line of code 'wn.update()'. If you
don't use it in the main loop, the turtle window
(tkinter window) will not update, ie, it will
freeze the window and won't update the canvas to
which your program is drawing to. Now, you maybe
asking 'What are two common errors?'. They are:

- turtle.Terminator error
- tkinter.TclError error

To understand this program you'll need prior
knowledge on error handling (try and except)in
python.

PS. I've spotted a pattern in how these two er-
rors vary from program to program. If the while
loop gets interrupted when it was running
'window.update()' line, it showed the error
'turtle.Terminator'. While running any other
pen related commands, it showed,
'tkinter.TclError'. I don't know if this obser-
vation will help anyone, but I just felt like
mentioning it anyway.

Code by: Sidharth S alias SidTheLoser.
Written on or before 20-Nov-2020.
Updated on 05-Aug-2022.

"""
