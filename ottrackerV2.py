#!/usr/bin/python3

from tkinter import * 
from tkinter import ttk 
import webbrowser
import boto3
import base64
import datetime
import time
import getpass
import json
import decimal
import sys
import os
from tkinter import messagebox

Time=time.strftime("%d-%m-%Y",time.gmtime())
uname = getpass.getuser()



def quit_window():  
   global opened,root
   
   opened = False
   window.withdraw() 
   if cmb.get() == "0.5":
       root.after(10000)     
       Main()	
   elif cmb.get() == "1":
       root.after(20000)
       Main()
   elif cmb.get()=="1.5":
       root.after(30000)
       Main()
   elif cmb.get() == "2":
       root.after(40000)
       Main()        

def return_main():  
    global opened
    window.withdraw()
    opened = True
    print(opened)
    Main()

#Kronos_link
def link(event):
        
    url="https://mytime-lite.aka.corp.amazon.com/wfc/applications/suitenav/navigation.do?ESS=true?redirect=/wfc/applications/wtk/html/ess/timestamp.jsp"
    webbrowser.open(url)
    root.destroy()

def exit():
    root.quit()


def mail():
    aa = b'QUtJQUkyNzQ3UDJLRjQ0TEhCQ1E='
    bb = base64.b64decode(aa)
    cc = bb.decode('UTF-8')
    ee = b'Rnlra0RlMWZDeHdvdUpxTktoNVhuT3BrdEFGaFlRLzRyNzhxTEV6Kw=='
    ff = base64.b64decode(ee)
    gg = ff.decode('UTF-8')
		
    Reason = str(entry_1.get("1.0","end"))
    t = len(Reason)
    p=int(t)
    print(p)
    Hours = str(cmb.get())
 
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
    window.quit()
    
        



global launch
def launch():
    global opened, window , cbox , cmb
    print(opened)
    if opened == True:
        
        window.deiconify()
        window.update()
        root.destroy()
    else:
        window = Tk()
        window.title("PUNCH-OUT Reminder")
        window.geometry("630x400+650+250")

        label_3= Label(window,text='Reason for staying Back     :',font= "Times 14 bold",fg="BLACK").place(x=30,y=50)

        global entry_1
        entry_1= Text(window,height=4,width=30)
        entry_1.place(x=350,y=40)

        label_4= Label(window,text='Extending Time (in Hours) (Ex: 1 or 1.5) :',font= "Times 14 bold",fg="BLACK").place(x=25,y=150)



        cmb = ttk.Combobox(window, width=20,height=4, values=("0.5","1","1.5","2"))
        cmb.place(x=370,y=150)  
        
        button3= Button(window,text="Back",font="Times 20 ",width=10,fg="BLACK",state='normal',command=return_main)
        button3.bind("<Button-3>")
        button3.place(x=120,y=220)


        button4= Button(window,text="Submit",font="Times 20 ",width=10,fg="BLACK",command=lambda:[mail() & quit_window()])
        button4.bind("<Button-4>")
        button4.place(x=360,y=220)
        

        root.destroy()  
        window.mainloop()



def Main():  
    global root
    print(opened)
    root = Tk()

    label_1=Label(root,text = "Hey, "+uname+ " ! ! ! " ,font= "Times 26 bold",fg="BLACK").place(x=180,y=40)
    
    label_2=Label(root,text= " \n It's Time to Leave, Do you want to PUNCH_OUT ? \n ",font ='Times 20',fg='BLACK').place(x=30,y=90)
    
    root.title("PUNCH-OUT Reminder")  
    root.geometry("630x400+650+250")
    
    button1= Button(root,text="Yes",font="Times 20 ",width=10,fg="BLACK")
    button1.bind("<Button-1>",link)
    button1.place(x=120,y=220)


    button2= Button(root,text="No ",font="Times 20 ",command= lambda:[exit(),launch()],state='normal',width=10,fg="BLACK")
    button2.bind("<Button-2>")
    button2.place(x=360,y=220)
    root.mainloop()

opened = False 
Main()  


