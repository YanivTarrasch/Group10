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
