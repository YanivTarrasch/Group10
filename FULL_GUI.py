from tinydb import TinyDB, Query
from spellchecker import SpellChecker
from random import random
from tkinter import *
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class User: #Class for the user player
    def __init__(self,player): #Init players data
        self.id=player[0]['ID']
        self.name=player[0]['Name']
        self.pwd=player[0]['Password']
        self.user=player[0]['User']
        self.AWAs=player[0]['AerageOfWAs']
        self.ASMs=player[0]['AerageOfSMs']
        self.GP=player[0]['GamePlayed']

    def signup_command(): #GUI window
        window = Tk()
        window.title("Sign up")

        l1 = Label(window, text="Name")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Username")
        l2.grid(row=2, column=0)

        l3 = Label(window, text="Password")
        l3.grid(row=4, column=0)    

        Name_text = StringVar()
        e1 = Entry(window, textvariable=Name_text)
        e1.grid(row=1, column=0)

        Username_text = StringVar()
        e2 = Entry(window, textvariable=Username_text)
        e2.grid(row=3, column=0)
   
        Password_text = StringVar()
        e3 = Entry(window, textvariable=Password_text)
        e3.grid(row=5, column=0)    

        b1 = Button(window, text="Create Account", width=12, command=login_command)
        b1.grid(row=6, column=0)
       
      
def firstchoices_command(player):

    window = Tk()
    window.title("TRIVIX")
    w,h=window.winfo_screenwidth() , window.winfo_screenheight()

    window.geometry((str(int(w)) + 'x' + str(int(h)))+'+0+0')
#window.geometry((str(int(w/4)) + 'x' + str(int(h/2)))+'+400+100')

    b1 = Button(window, text="Play Game", width=12, command=lambda:Question_command(player,window))
    b1.grid(row=1, column=1)

   
    window.mainloop()
    

def homePage(win):#Home page for login or signup choise    

    window = Tk()
    window.title("Welcome to TRIVIX Game!!")
    w,h=window.winfo_screenwidth() , window.winfo_screenheight()
    window.geometry((str(int(w/4)) + 'x' + str(int(h/2)))+'+400+100')
    b1 = Button(window, text="Log In", width=12,bg="gray", command=lambda:login_command(window))
    b1.grid(row=1, column=1)
    
    OPTIONS = ["Signup","Child","Parent"] #Example for menu option
    variable = StringVar(window)
    variable.set(OPTIONS[0]) # default value
    
    m = OptionMenu(window, variable, *OPTIONS)
    m.place(relx=0.5, rely=0.5,x=0,y=40, anchor=CENTER)

    def callback(*args):
        if(variable.get())=="Child":
            SignUp_command(window)
        elif(variable.get())=="Parent":
            SignUp_command_P(window)

    variable.trace("w", callback)

   
    b1.place(relx=0.5, rely=0.5, anchor=CENTER)
   
    if(win!=0):
        win.destroy()
    window.mainloop()

def login_command(wid): #Login Window, this is the GUI after the main menu that you login - NO SIGN UP HERE!!
    
        window = Tk()
    
        window.title("Login")
        w,h=window.winfo_screenwidth() , window.winfo_screenheight()
        window.geometry((str(int(w/4)) + 'x' + str(int(h/2)))+'+400+100')
       
        l1 = Label(window, text="Username")
        l1.place(relx=0.5, rely=0.5,x=-35,y=-80,  anchor=CENTER)

        l2 = Label(window, text="Password")
        l2.place(relx=0.5, rely=0.5,x=-35,y=-40,  anchor=CENTER)

        Username_text = StringVar()
        e1 = Entry(window, textvariable=Username_text)
        e1.place(relx=0.5, rely=0.5,x=0,y=-60,  anchor=CENTER)

        Password_text = StringVar()
        e2 = Entry(window, textvariable=Password_text,show='*')
        e2.place(relx=0.5, rely=0.5,x=0,y=-20, anchor=CENTER)
    
        b3 = Button(window, text="Login", width=12,bg="gray", command=lambda:onClick(e1.get(),e2.get(),window))
   # b3.grid(row=2, column=1)
        b3.place(relx=0.5, rely=0.5,x=0,y=20, anchor=CENTER)

        b2 = Button(window, text="Back", width=12,bg="gray", command=lambda:homePage(window))
        b2.place(relx=0.5, rely=0.5,x=0,y=100, anchor=CENTER)

        wid.destroy()
        window.mainloop()
    
def insertPlayer(name,pwd,id,pid): #Insert a new Player To database
    w=Tk()
    w.geometry("0x0")
    if len(name)<1 or len(pwd)<1 or len(pid)<1:
           messagebox.showerror(title='Failure', message='Please Fill All Fields')
           w.destroy()
           return
    if( ptb.search(query.ID==int(pid))==[]):
      
       messagebox.showerror(title='Error', message='Parent With Given ID not exist')

    elif( tb.search(query.ID==int(id))!=[]):
      
       messagebox.showerror(title='Error', message='User With Given ID already exist')
        
    else:
        usr = {'ID':int(id),'Password':pwd,'Name': name,'User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':int(pid)}
        tb.insert(usr)
        def msg():
            
            tk.messagebox.showinfo(title='Success', message='Player Successfuly Registered')
        msg()
    w.destroy()#Creates Player
    
def insertParent(name,pwd,id):#Insert a new Parent To database
        w=Tk()
        w.geometry("0x0")
        if len(name)<1 or len(pwd)<1:
           messagebox.showerror(title='Failure', message='Please Fill All Fields')
           w.destroy()
           return
    
        usr = {'ID':int(id),'Password':pwd,'Name': name,'User':'Parent', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
        parent = {'ID':int(id),'Name': name,'Child':[]}
        tb.insert(usr)
        ptb.insert(parent)
       
        messagebox.showinfo(title='Success', message='Parent Successfuly Registered')
        w.destroy()#Creates Parent

def parentView(parent):
    window=Tk()
   
    id=parent.id
    b1 = Button(window, text="Make Question", width=12,bg="gray", command=lambda:Add_Question())
    #b1.place(relx=0, rely=0,x=-50,y=15)
    b1.grid(row=1,column=0)
    b2 = Button(window, text="LogOut", width=12,bg="blue", command=lambda:(window.destroy()))
    #b2.place(relx=1,rely=0,x=-50,y=15)
    b2.grid(row=1,column=1 )
    p=tb.search((query.User=='Player')&(query.ParentID==parent.id))
    showStats(window,p)
    window.mainloop()
def ManagerView(parent):
    window=Tk()
    id=4
    
    b1 = Button(window, text="Make Question", width=12,bg="gray", command=lambda:Add_Question())
    #b1.place(relx=0, rely=0,x=-50,y=15)
    b1.grid(row=1,column=0)
    b2 = Button(window, text="LogOut", width=12,bg="blue", command=lambda:(window.destroy()))
    #b2.place(relx=1,rely=0,x=-50,y=15)
    b2.grid(row=1,column=1 )
    p=tb.search((query.User=='Player'))
    showStats(window,p)
    
    window.mainloop()
    
homePage(0)
time.sleep(11)

