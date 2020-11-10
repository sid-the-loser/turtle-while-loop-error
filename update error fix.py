import turtle

wn = turtle.Screen()
wn.tracer(0)

player = turtle.Turtle()

while True: # You can use other stuff other than True
    try: # Make sure to put all your looping code in this
        wn.update()
        player.right(30)
    except Exception as e: # If the update brings up an error; this stops the error from showing up at all
        print(e) # This prints out the error
        break # This just breaks the loop

# Important!
#-----------------------

"""(Im refering to line 13 here)I do understand that you will ask me, "Why would you wanna print out the error if we are trying to get rid of it in the first place!".
I did that because people are not perfect and they could make errors in the codes that they right, if you make any error other than the update error, the window
will just close and you will bhe left all confuced on what happened, that is why I printed out the error. This line (line 13) is only used for debugging purposes and 
after you are done with you are done with your code (if you done the whole coding and you are going to publish the code to executable or anything else you can get rid of
that print statement"""
