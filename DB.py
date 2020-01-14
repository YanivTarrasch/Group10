#Import the TinyDB module and submodules
from tinydb import TinyDB, Query
 

#Declare our database variable and the file to store our data in
def getConnection(str):
    db = TinyDB(str+'.json')
    return db



db=getConnection('Game')
#db=getConnection('myDB')
tb=db.table('User') #user table
tbq=db.table('Questions') #Question table
tbp=db.table('Parent') #parent table


#default users
usr1 = {'ID':1,'Password':'1','Name': 'Avi','User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}
usr2 = {'ID':2,'Password':'2','Name': 'Yossi','User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}
usr3 = {'ID':3,'Password':'3','Name': 'Natan','User':'Player', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':6}
usr4 = {'ID':4,'Password':'4','Name': 'Chen','User':'Parent', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
usr5 = {'ID':5,'Password':'5','Name': 'Yaniv','User':'Manager', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
usr6 = {'ID':6,'Password':'6','Name': 'Itay','User':'Parent', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}


class testDB(unittest.TestCase): #unit test! of default users 
    #testing test
    def test1(self): 
        self.assertEqual(1,1)
    def test2(self):
        self.assertNotEqual(1,5)
        
     #test Question In tbq
    def test_Q1(self):
        self.assertIn(Q1,tbq)
    def test_Q2(self):
        self.assertIn(Q2,tbq)
    def test_Q3(self):
        self.assertIn(Q3,tbq)
    def test_Q4(self):
        self.assertIn(Q4,tbq)
    def test_Q5(self):
        self.assertIn(Q5,tbq)
      
    #test Question Not In tbq
    def test_Not_Q1(self):
        self.assertNotIn({'ID':6,'Question':'test test ','Answer': 'aaaaaaaaa','Points':5},tbq)
    def test_Not_Q2(self):
        self.assertNotIn({'ID':5,'Question':' is the top colour in a rainbow? ','Answer': 'gold','Points':3},tbq)
    def test_Not_Q3(self):
        self.assertNotIn({'ID':7,'Question':'Who are You?? ','Answer': 'im IronMan!!!!!','Points':3},tbq)
    def test_Not_Q4(self):
        self.assertNotIn({'ID':1,'Question':'Who we gonna call?? ','Answer': 'GhostBusters!','Points':3},tbq)
    def test_Not_Q5(self):
        self.assertNotIn({'ID':2,'Question':'what is the first rule in fightClub? ','Answer': 'You dont talk about fightClub','Points':3},tbq) 
      
    #test users role
    def test_role1(self):
        self.assertEqual(usr1['User'],'Player')
    def test_role2(self):
        self.assertEqual(usr2['User'],'Player')
    def test_role3(self):
        self.assertEqual(usr3['User'],'Player')
    def test_role4(self):
        self.assertEqual(usr4['User'],'Parent')
    def test_role5(self):
        self.assertEqual(usr5['User'],'Manager')
    def test_role6(self):
        self.assertEqual(usr6['User'],'Parent')
      
    #test users Name and ID
    def test_usr1(self):
        self.assertTrue((usr1['Name'] == 'Avi') and (usr1['ID'] == 1))
    def test_usr2(self):
        self.assertTrue((usr2['Name'] == 'Yossi') and (usr2['ID'] == 2))
    def test_usr3(self):
        self.assertTrue((usr3['Name'] == 'Natan') and (usr3['ID'] == 3))
    def test_usr4(self):
        self.assertTrue((usr4['Name'] == 'Chen') and (usr4['ID'] == 4))
    def test_usr5(self):
        self.assertTrue((usr5['Name'] == 'Yaniv') and (usr5['ID'] == 5))
    def test_usr6(self):
        self.assertTrue((usr6['Name'] == 'Itay') and (usr6['ID'] == 6))
      
    #test Parent in tbp
    def test_tbp1(self):
        self.assertIn(p1,tbp)
    def test_tbp2(self):
        self.assertIn(p2,tbp)
      
    #test Parent , child
    def test_par1(self):
        self.assertEqual(p1['child'],[1,2])
    def test_par2(self):
        self.assertEqual(p2['child'],[3])
    
 if __name__ == '__main__': 
    unittest.main() #start unit test 

#Insert 4 reords into our todo list database

#tbq.insert(Q1)
#tbq.insert(Q2)
#tbq.insert(Q3)
#tbq.insert(Q4)
#tbq.insert(Q5)

#tb.insert(usr1)
#tb.insert(usr2)
#tb.insert(usr3)
#tb.insert(usr4)
#tb.insert(usr5)
#tb.insert(usr6)

#tbp.insert(p1)
#tbp.insert(p2)

#print(tb.all())
#print(tbq.all())
#print(tbp.all())
