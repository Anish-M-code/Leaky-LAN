from sqlite3 import *
import functools
import operator
class user_auth(object):
    
   def __init__(name,email,password,self):
        name = self.name;
        email = self.email;
        password = self.password;
   
   User = connect("User_database.db")
   conn = User.cursor()
   
   def create_db():
       User = connect("User_database.db")
       conn = User.cursor()
       conn.execute("""CREATE TABLE user_db(
    name text,
    email text unique ,
    password text)""")
       return(0)
    
   
   def signup(Name,Email,Password):

        User = connect("User_database.db")
        conn = User.cursor();
        conn.execute("""Insert into user_db(name,email,password)
values('%s',
'%s',
'%s');"""%(Name,Email,Password))
        User.commit()
        return(0)

   def authenticator(email,password):
       User = connect("User_database.db")
       conn = User.cursor()
       conn.execute("""select password from user_db where email is '%s' """%(email))
       dat = functools.reduce(operator.add,conn.fetchone())
       if(password==dat):
                print("success")
       else :
            print("Authentication failed")
            User.close()
            





    
   
        
        

