# Turtle While Loop Error (while doing a turtle window.update()) 
There are two common types of errors that turtle makes when you close its window while running a while loop. This error is caused due to an un-avoidable line of code 'wn.update()'. If you don't use it in the main loop, the turtle window (tkinter window) will not update, ie, it will freeze the window and won't update the canvas to which your program is drawing. Now, you may ask 'What are two common errors?'. They are:

- turtle.Terminator error
- tkinter.TclError error

To understand this program you'll need prior knowledge of error handling (try and except)in python.

PS. I've spotted a pattern in how these two errors vary from program to program. If the while loop gets interrupted when it is running 'window.update()' line, it shows the error 'turtle.Terminator'. While running other pen-related commands, it showed, 'tkinter.TclError'. I don't know if this observation will help anyone, but I just felt like mentioning it anyway.
