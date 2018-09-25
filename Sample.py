

"""I'm trying to hide my window and show it back if it was open before.

For that, I'm using a global variable opened but this one is not behaving like I want.

For example, when I return from my window and go back my variable is False instead of the True I'm expecting.

I'm using Python 3.6 with Tkinter And down here is the code.

If someone, can explain to me why it´s behaving this way or what I did wrong, It will be nice of you. Thanks.

I know this blog is showing a way to do that but I want to understand why this way is not working, thanks."""

from tkinter import * 

def quit_window():  
   window.destroy()
   opened = False
   Main()



def return_main():  
    window.withdraw()
    opened = True
    print(opened)
    Main()

def launch():
    global opened, window
    print(opened)
    if opened == True:
        window.update()
        window.deiconify()
        main.destroy()
    else:
        window = Tk() 
        breturn = Button(window, text="Return", command=return_main).pack()
        bquit = Button(window, text="Quit", command=quit_window).pack() 
        main.destroy()
        window.mainloop()



def Main():  
    global main
    print(opened)
    main = Tk()  
    bopen = Button(main, text="Open", command=launch).pack() 
    main.mainloop()

opened = False 
Main()  


