#!/usr/bin/python3

from tkinter import *


def cron():
    root=Tk()
    root.geometry("630x400+650+250")

    entry_1= Text(root,height=4,width=30)
    entry_1.place(x=350,y=40)

    def exit():
        #root.withdraw()
        root.quit()
    def value():

        Time = str(entry_1.get("1.0","end"))
        
        a= int(Time)*10000
        if (button2 !='normal'):
            root.after(a,lambda:cron())
            root.withdraw()
            



    button2= Button(root,text="Remind me after 5 Minutes ",font="Times 16",state='normal',command=value)
    button2.bind("<Button-2>")
    button2.pack()

    button3= Button(root,text="Close ",font="Times 20 ",width=10,fg="BLACK",command= exit)
    button3.bind("<Button-3>")
    button3.place(x=360,y=220)



    root.mainloop()
    root.quit()
cron()




