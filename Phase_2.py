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
import random
import datetime
import base64
import webbrowser




Time=time.strftime("%d-%m-%Y",time.gmtime())
uname = getpass.getuser()

def window_one():
    global root
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


    def exit():
        root.destroy() #destroy
    

    def disable_event_1():
        pass

    button1= Button(root,text="Yes",font="Times 20 ",width=10,fg="BLACK")
    button1.bind("<Button-1>",link)
    button1.place(x=120,y=220)


    button2= Button(root,text="No ",font="Times 20 ",command=lambda:[exit(), window_two()] ,state='normal',width=10,fg="BLACK")
    button2.bind("<Button-2>")
    button2.place(x=360,y=220)
    root.protocol("WM_DELETE_WINDOW",disable_event_1)
    root.after(14400000,lambda:root.destroy())
    root.mainloop()

def window_two():
    
    master =Tk()
    master.title("PUNCH-OUT Reminder")
    master.geometry("630x400+650+250")
    master.configure()
    


    label_3= Label(master,text='Reason for staying Back     :',font= "Times 14 bold",fg="BLACK").place(x=30,y=50)

    global entry_1
    entry_1= Text(master,height=4,width=30)
    entry_1.place(x=350,y=40) #,height=4
    
    label_4= Label(master,text='Extending Time (in Hours) (Ex: 1 or 1.5) :',font= "Times 14 bold",fg="BLACK").place(x=25,y=150)

    global entry_2
    entry_2= Text(master,height=2,width=30)
    entry_2.place(x=350,y=150) #height=2,
    
    def disable_event_2():
        pass

    def exit_2():
        master.destroy()

    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if abs(o) % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)

    def mail():
        aa = b'QUtJQUpaRzJHVzJZNkNKNTNUWUE='
        bb = base64.b64decode(aa)
        cc = bb.decode('UTF-8')
        ee = b'ZndpOWEyYXdRenNQSGNiOEYydFZmL0hRVkNucVIrN1BoU3hPZVgvOA=='
        ff = base64.b64decode(ee)
        gg = ff.decode('UTF-8')
		
        Reason = str(entry_1.get("1.0","end"))
        t = len(Reason)
        Hours = str(entry_2.get("1.0","end"))
        m = len(Hours)

        def Iter():
            Reg= int(Hours)*10000
            if (button3 !='normal'):
                root.after(Reg,lambda:window_one())
                #root.withdraw()

        if t > 2 and m > 1: 
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
            print(json.dumps(response, indent=4, cls=DecimalEncoder))
            master.quit()
			
        else:
            messagebox.showinfo("Error", "Please fill Extended hours and Reason for extending")

    button3= Button(master,text="Submit",font="Times 20 ",width=10,fg="BLACK",state='normal',command=mail)
    button3.bind()
    button3.place(x=120,y=220)


    button4= Button(master,text="No ",font="Times 20 ",width=10,fg="BLACK",command= exit_2)
    button4.bind("<Button-4>")
    button4.place(x=360,y=220)
    master.protocol("WM_DELETE_WINDOW",disable_event_2)
    master.after(14400000,lambda:master.destroy())
    master.mainloop()
    master.withdraw()
    
window_one()    
