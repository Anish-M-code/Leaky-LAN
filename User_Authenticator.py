#user authentication Engine using MySQL datase

import mysql.connector as conn
from random import randint

def pass_gen() -> str:
    passwd = ''.join(chr(randint(33, 126)) for _ in range(6))
    return passwd


# Authentication class used for both server and client side

class user_db(object):
    def __init__(self, host, username, password) -> None:
        self.mydb = conn.connect(
            host=host,  # Specify the IP address or hostname here
            user=username,
            password=password
        )
        self.cursor = self.mydb.cursor(buffered=True)
    
    #used in server script
    def server_side(self,user):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS Authorization")
            self.mydb.commit()
            self.cursor.execute("USE Authorization")
            self.mydb.commit()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Auth (user VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL)")
            self.mydb.commit()
        except conn.Error as e:
            print('Check your Mysql Server')
        finally:
            passwd = pass_gen()
            try :
                self.cursor.execute('Insert into Auth(user,password) values(%s,%s)',(user,passwd))
                print('The password is : '+passwd)
                print('Share this password with your user')
                self.mydb.commit()
            except :
                self.cursor.execute('Select password from Auth where user = %s',(user,))
                self.mydb.commit()
                query = self.cursor.fetchone()
                self.mydb.commit()
                print('User already Exists with password : ' + query[0])
                print('Share this password with your user')
            
            self.cursor.close()
            self.mydb.close()
    
    #create a new client object in client script to execute it

    def client_side(self,user,password):
        self.cursor.execute('USE Authorization')
        self.mydb.commit()
        self.cursor.execute('Select password from Auth where user = %s',(user,))
        self.mydb.commit()
        query = self.cursor.fetchone()
        if query[0] != password :
            print('Wrong Password')
            self.cursor.close()
            self.mydb.close()
            return 0
        else :
            print('User Authentication Sucessfull')
            self.cursor.close()
            self.mydb.close()
            return 1
        
    










    
   
        
        

