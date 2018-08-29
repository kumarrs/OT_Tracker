#!/usr/bin/python3

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import sys
import os
import getpass
import time
import pymongo 
import webbrowser
import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify






Time=time.strftime("%d-%m-%Y",time.gmtime())
uname = getpass.getuser()

def window_one():
    
    root=Tk()
    root.title("PUNCH-OUT Reminder")
    root.geometry("630x400+650+250")
    root.configure()
    
    label_1=Label(root,text = "Hey, "+uname+ " ! ! ! " ,font= "Times 26 bold",fg="BLACK").place(x=180,y=40)
    
    label_2=Label(root,text= " \n It's Time to Leave, Do you want to PUNCH_OUT ? \n ",font ='Times 20',fg='BLACK').place(x=30,y=90)
    

    def link(event):
        
        url="https://mytime-lite.aka.corp.amazon.com/wfc/applications/suitenav/navigation.do?ESS=true?redirect=/wfc/applications/wtk/html/ess/timestamp.jsp"
        webbrowser.open(url)
        root.quit()
        Notify.init('Time_OFF_Notification')
        pop_up=Notify.Notification.new("Hi " +uname+ " !" ,"Click on the 'Record Time Stamp' button to Punch-OUT",'/home/local/ANT/kumarrs/Aces/amazon.png')	
        pop_up.show()
        pop_up.set_urgency(2)

    def exit():
        root.destroy()

    button1= Button(root,text="Yes",font="Times 20 ",width=10,fg="BLACK")
    button1.bind("<Button-1>",link)
    button1.place(x=120,y=220)


    button2= Button(root,text="No ",font="Times 20 ",command=lambda:exit() & window_two(),state='normal',width=10,fg="BLACK")
    button2.bind("<Button-2>")
    button2.place(x=360,y=220)
    
    root.mainloop()

def window_two():
    
    master =Tk()
    master.title("PUNCH-OUT Reminder")
    master.geometry("630x400+650+250")
    master.configure()

    label_3= Label(master,text='Reason for staying Back :',font= "Times 20 bold",fg="BLACK").place(x=30,y=50)

    entry_1= Text(master,width=30,height=4).place(x=350,y=40)
    
    label_4= Label(master,text='Extending time (in Hours) :',font= "Times 20 bold",fg="BLACK").place(x=30,y=150)

    entry_2= Text(master,height=2,width=30).place(x=350,y=150)

    def database():
        Reason = str(entry_1.get())
        Hours = str(entry_2.get())
    
        
        Client= pymongo.MongoClient("mongodb://admin:password@localhost:27017") #mongodb://admin:password@localhost:27017/
                                                                                            # mongodb://172.31.80.100:27017
        mydb = Client["Final"]

        mycol=  mydb[Time]
        mydict= {"name":uname,"hours":Hours,"reason":Reason}
        x = mycol.insert(mydict)
        print(x)
        master.destroy()

    button3= Button(master,text="Yes",font="Times 20 ",width=10,fg="BLACK")
    button3.bind("<Button-1>",database)
    button3.place(x=120,y=220)


    button4= Button(master,text="No ",font="Times 20 ",command=lambda:exit(),state='normal',width=10,fg="BLACK")
    button4.bind("<Button-2>")
    button4.place(x=360,y=220)

    master.mainloop()


window_one()    
