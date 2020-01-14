from tinydb import TinyDB, Query
from spellchecker import SpellChecker
from random import random
from tkinter import *
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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