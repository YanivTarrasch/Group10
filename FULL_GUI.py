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