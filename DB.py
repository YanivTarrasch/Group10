#Import the TinyDB module and submodules
from tinydb import TinyDB, Query
 

#Declare our database variable and the file to store our data in
def getConnection(str):
    db = TinyDB(str+'.json')
    return db



db=getConnection('Game')
#db=getConnection('myDB')
tb=db.table('User')
tbq=db.table('Questions')
tbp=db.table('Parent')



usr1 = {'ID':1,'Password':'1','Name': 'Avi','User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}
usr2 = {'ID':2,'Password':'2','Name': 'Yossi','User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}
usr3 = {'ID':3,'Password':'3','Name': 'Natan','User':'Player', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':6}
usr4 = {'ID':4,'Password':'4','Name': 'Chen','User':'Parent', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
usr5 = {'ID':5,'Password':'5','Name': 'Yaniv','User':'Manager', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
usr6 = {'ID':6,'Password':'6','Name': 'Itay','User':'Parent', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}


