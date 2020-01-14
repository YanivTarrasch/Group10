#Import the TinyDB module and submodules
from tinydb import TinyDB, Query
 

#Declare our database variable and the file to store our data in
def getConnection(str):
    db = TinyDB(str+'.json')
    return db
