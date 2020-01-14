from tinydb import TinyDB, Query
from spellchecker import SpellChecker
from random import random
from tkinter import *
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#default DB with very first users and questions 
#import DB


def getConnection(str): #getting a connection to our DB
    db = TinyDB(str+'.json')
    return db

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
       
def getQuestions():
      qtb=mdb.table('Questions')
      questions=[]
      for Q in qtb:
          questions.append([Q['Question'],Q['Answer'],Q['Points']])
      return questions      

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
        
def onClick(name,pwd,wind): 
     usr=Query()
     
     rs=tb.search((usr.Name == name) & (usr.Password==pwd))
    
     print (rs)
     if rs!=[] and rs[0]['User']=='Player':
         player=User(rs)
         firstchoices_command(player)
         wind.destroy()
     elif rs!=[] and rs[0]['User']=='Manager':
         player=User(rs)
         ManagerView(player)
         wind.destroy()
     elif rs!=[] and rs[0]['User']=='Parent':
         player=User(rs)
         parentView(player)
         wind.destroy()
     else:
         loginError() 
    

def genrateID():
    #return max id to next insernt in DB
    table=tb.search(query.ID!=[])
    ids=[]
    for i in table:
        ids.append(i['ID'])
        

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

def Question_command(player,window,rv={'Score':0,'SpellMs':0,'Index':0,'QNo':0,'WAns':0,'Attempts':0}): #shows 5 question and gives an oppertunity for 3 times
        
        score=rv['Score']
        #window = Tk()
       
        if(rv['Index']<5):
            questions=getQuestions()
            attempts=3
            ques=5
            if(rv['Attempts'] in [0,3] ):
                rv['Index']=rv['Index']%len(questions)
                index= ((random()%((len(questions))-rv['Index']))+rv['Index'])
                rv['Attempts']=0
            else:
                index=rv['Index']
            l1 = Label(window, text="Question")
            l1.place(relx=0.5, rely=0.5,x=-35,y=-80,  anchor=CENTER)

            l2 = Label(window, text="Amswer")
            l2.place(relx=0.5, rely=0.5,x=-35,y=-40,  anchor=CENTER)
            
            Username_text = StringVar()
            S = tk.Scrollbar(window)
           
            l3 = Text(window)
            l3.place(relx=0.5, width=window.winfo_width()-5, rely=0.5,x=0,y=-60,  anchor=CENTER)
            l3.insert( tk.END,questions[int(index)][0])
            
            l4 = Label(window,bg='gray', text='Score: '+str(score))
            l4.place( relx=0.5, rely=0,x=0,y=0)
       
            Password_text = StringVar()
            e2 = Entry(window, textvariable=Password_text)
            e2.place(relx=0.5, rely=0.5,x=0,y=-20, anchor=CENTER)
        
            b2 = Button(window, text="LogOut", width=12,bg="blue", command=lambda:homePage(window))
            b2.place(relx=1, rely=0,x=-50,y=15, anchor=CENTER)
            b3 = Button(window, text="Submit", width=12,bg="gray", command=lambda:Checker(e2.get(),questions[int(index)],rv,window,player))
            b3.place(relx=0.5, rely=0.5,x=0,y=20, anchor=CENTER)
        else:
            w=Tk()
            w.geometry("0x0")
            p=tb.search(query.ID==player.id)[0]
            print(p)
            GP=p['GamePlayed']
            if GP==0:
                GP=1
            update={'AerageOfWAs':((p['AerageOfWAs']*p['GamePlayed'])+rv['WAns'])/GP, 
                      'AerageOfSMs':((p['AerageOfSMs']*p['GamePlayed'])+rv['SpellMs'])/GP,
                      'GamePlayed':(p['GamePlayed']+1)}
            tb.update(update,query.ID==p['ID'])
            messagebox.showinfo(title='Game Over', message='You Score: '+str(score)+' Points'+' With Spell Mistakes: '+str(rv['SpellMs']))
            print(rv)
            w.destroy()
            window.destroy()
            rv.update({'Score':0,'SpellMs':0,'Index':0,'QNo':0,'WAns':0,'Attempts':0})
            
            print(rv)
            rs=tb.search(query.ID==player.id)
            player=User(rs)
            #firstchoices_command(player)// Lets see if it works without this "LOOP"

def Checker(ans,question,rv,win,player):
    if rv['Index']==5:
        return
    misspelled = spell.unknown(ans)
    print(misspelled)
    print(spell.correction(ans))
    print(question[1])
    w=Tk()
    w.geometry("0x0")
    if(question[1].lower()==(spell.correction(ans)).lower()):
        print(spell.correction(question[1]))
        rv['Score']=rv['Score']+question[2]
        #points
        rv['Attempts']=0
        rv['Index']=rv['Index']+1
        rv['QNo']=rv['QNo']+1
        if(ans.lower()!=question[1].lower() and question[1].lower()==(spell.correction(ans)).lower()):
            rv['SpellMs']=rv['SpellMs']+1
            rv['Score']=rv['Score']-1
            #spell Mistakes
        #else:
            #rv['SpellMs']=0
        messagebox.showinfo(title='Congrats!', message='Right Answer You Got: '+str(rv['Score'])+' Points'+' With Spell Mistakes: '+str(rv['SpellMs']))

    else:
        rv['Attempts']=rv['Attempts']+1
        if(rv['Attempts']==3):
            rv['WAns']=rv['WAns']+1
            rv['Index']=rv['Index']+1
        #Wrong Ans
        messagebox.showinfo(title='Opps!', message='Wrong Answer You Left: '+str(3-rv['Attempts'])+' Chances')

    print(rv)    
    w.destroy()
    Question_command(player,win,rv)            
            
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

def parentView(parent):#GUI For parent to see childs info
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
    
def showStats(scores,stats):
    #scores = tk.Tk() 
    label = tk.Label(scores, text="Game Scores", font=("Arial",30)).grid(row=3, columnspan=3)
    # create Treeview with 3 columns
    cols = ('ID', 'Name', 'Average Wrong Answer', 'Average Spell Mistakes','Game Played')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    # set column headings
    for col in cols:    
        listBox.heading(col, text=col)  
    for x in stats:
       listBox.insert("", "end", values=(x['ID'], x['Name'], x['AerageOfWAs'],x['AerageOfSMs'],x['GamePlayed']))
    listBox.grid(row=4, column=0, columnspan=2)

    scores.mainloop()
homePage(0)
time.sleep(11)

