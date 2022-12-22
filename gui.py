from tkinter import *
import ipaddress
import pand
import atexit
def chk_ip(ip_str):  
   try:  
       ip_obj = ipaddress.ip_address(ip_str)  
       return True  
   except ValueError:  
       return False
class Myapp:
    def __init__(self,root):
        global entrytext
        #basic geometry setup
        root.title("object detection")
        root.geometry("300x300")
        root.maxsize(300,300)
        #variables for getter and setter variables
        self.connecstat=StringVar()
        self.color=StringVar()
        #tkinter elements
        labelconn=Label(root,textvariable=self.connecstat)
        label=Label(root,text="enter ip adress")
        label.pack()
        self.entrytext=StringVar()
        entry=Entry(root,textvariable=self.entrytext)
        entry.pack()
        button=Button(root,text="connect",command=self.gdata)
        button.pack()
        labelconn.pack()
    def gdata(self):
       #verify and write ip adress
        ip_str=self.entrytext.get()
        if chk_ip(ip_str):
            self.connecstat.set("connecting.....")
            pand.sip(ip_str)
        else:
            self.connecstat.set("enter valid ip")
               
        
root=Tk()
#calling tje class
Myapp(root)
root.mainloop()
