#!/usr/bin/python3

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import sys
import os
import getpass
import time
import boto3
import json
import decimal
import datetime
import base64
import webbrowser
import dynamo

uname = getpass.getuser()

global mail
def mail():
        
        aa = b'QUtJQUpaRzJHVzJZNkNKNTNUWUE='
        bb = base64.b64decode(aa)
        cc = bb.decode('UTF-8')
        ee = b'ZndpOWEyYXdRenNQSGNiOEYydFZmL0hRVkNucVIrN1BoU3hPZVgvOA=='
        ff = base64.b64decode(ee)
        gg = ff.decode('UTF-8')
		
        """Reason = str(entry_1.get("1.0","end"))
        t = len(Reason)
        Hours = str(entry_2.get("1.0","end"))
        m = len(Hours)"""
        Hours=4
        Reason="Test Data"


        dynamodb = boto3.resource("dynamodb", aws_access_key_id=cc, aws_secret_access_key=gg, region_name='us-east-2', endpoint_url="http://dynamodb.us-east-2.amazonaws.com")
        table = dynamodb.Table('Test_Table_Phase2')
        now = datetime.datetime.now()
        curdat = now.strftime("%m-%d-%Y")
        b = uname+" "+str(now)
		
        uid = b
        unames = uname
        credat = curdat
        exhours = 5


        response = table.put_item(
        Item={
	    'uid': uid,
	    'uname': unames,
	    'credat': credat,
	    'exhours': Hours,
        'reason': Reason
        }
        )

        print("PutItem succeeded:")
        #print(json.dumps(response, indent=4, cls=DecimalEncoder))

def quit_window():  
   global opened
   opened = False
   mail()
   
   window.destroy()
   window.update	
   root.after(10000)
   Main()	
   

def return_main():  
    global opened
    window.withdraw()
    opened = True
    print(opened)
    Main()

def launch():
    global opened,window,entry_1,entry_2
    print(opened)
    if opened == True:
        window.update()
        window.deiconify()
        root.destroy()
    else:
	    
        window =Tk()
        window.title("PUNCH-OUT Reminder")
        window.geometry("630x400+650+250")
        window.configure()
    	
        root.destroy()


        label_3= Label(window,text='Reason for staying Back     :',font= "Times 14 bold",fg="BLACK").place(x=30,y=50)

        global entry_1
        entry_1= Text(window,height=4,width=30)
        entry_1.place(x=350,y=40) 
    
        label_4= Label(window,text='Extending Time (in Hours) (Ex: 1 or 1.5) :',font= "Times 14 bold",fg="BLACK").place(x=25,y=150)

        global entry_2
        entry_2= Text(window,height=2,width=30)
        entry_2.place(x=350,y=150) 
		
        button_3=Button(window,text="Back",font="Times 20 ",width=10,fg="BLACK",state='normal',command=return_main)
        button_3.bind()
        button_3.place(x=120,y=220)

        button_4=Button(window,text="Submit",font="Times 20 ",width=10,fg="BLACK",command=quit_window)
        button_4.bind()
        button_4.place(x=360,y=220)
        window.mainloop()


def Main():  
    global root
    print(opened)
    root = Tk()  
    root.title("PUNCH-OUT Reminder")
    root.geometry("630x400+650+250")
    root.configure()
    


    label_1=Label(root,text = "Hey, "+uname+ " ! ! ! " ,font= "Times 26 bold",fg="BLACK").place(x=180,y=40)
    
    label_2=Label(root,text= " \n It's Time to Leave, Do you want to PUNCH_OUT ? \n ",font ='Times 20',fg='BLACK').place(x=30,y=90)
    
    def link(event):
        
        url="https://mytime-lite.aka.corp.amazon.com/wfc/applications/suitenav/navigation.do?ESS=true?redirect=/wfc/applications/wtk/html/ess/timestamp.jsp"
        webbrowser.open(url)
        root.destroy()



    button1= Button(root,text="Yes",font="Times 20 ",width=10,fg="BLACK")
    button1.bind("<Button-1>",link)
    button1.place(x=120,y=220)


    button2= Button(root,text="No ",font="Times 20 ",command=launch,state='normal',width=10,fg="BLACK")
    button2.bind("<Button-2>")
    button2.place(x=360,y=220)
    root.mainloop()

opened = False 
Main()  


