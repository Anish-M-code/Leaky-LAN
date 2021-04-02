
# Leaky LAN
# Copyright (C) 2019-2020 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
A simple file sharing service using python http.server and cgi module
developed by M.Anish <aneesh25861@gmail.com> to avoid third party code .

'''
import os
import sys
import platform

# To clear screen.
os.system('cls' if platform.system().lower() == 'windows' else 'clear')

print('''

##       ########    ###    ##    ## ##    ##    ##          ###    ##    ## 
##       ##         ## ##   ##   ##   ##  ##     ##         ## ##   ###   ## 
##       ##        ##   ##  ##  ##     ####      ##        ##   ##  ####  ## 
##       ######   ##     ## #####       ##       ##       ##     ## ## ## ## 
##       ##       ######### ##  ##      ##       ##       ######### ##  #### 
##       ##       ##     ## ##   ##     ##       ##       ##     ## ##   ### 
######## ######## ##     ## ##    ##    ##       ######## ##     ## ##    ## 


                      Simple File sharing over LAN.
           
              Developed by M.Anish <aneesh25861@gmail.com>  
 
 Note: Files shared using this tool is available to each and every device 
 connected to LAN. Don't use on public Networks! 
              
''')

def getip(port = ':8000'):
    flag=0
    # Code specific to windows operating system.
    if platform.system().lower() == 'windows':
        os.system('ipconfig >temp.txt')
        if os.path.exists('temp.txt'):
            with open('temp.txt') as f:
                buff = f.readlines()
                for x in range(len(buff) - 1):

                     # To get ip address if user is connected to ethernet or wifi and ignore all other network interfaces.
                    if 'Ethernet adapter Ethernet' in buff[x] or 'Wireless LAN adapter' in buff[x]:
                        for i in range(6):
                            x += 1
                            try:
                                if 'IPv4' in buff[x]:
                                    print('Enter in Browser :',buff[x].split()[-1],port)
                                    flag = 1
                                    break

                            # Ignore index errors , it wont affect program functionality anyway.     
                            except IndexError:
                                pass
                    
            os.remove('temp.txt')

        # error message incase temp.text couldnot be created.                           
        else:
            print('Permission Denied!')
    else:
          os.system('ip a >temp.txt')
          if os.path.exists('temp.txt'):
              with open('temp.txt') as f:
                  for x in f:
                      if ('inet ' in x) and ('127.0.0.1' not in x):
                          print('Enter in Browser :',x.split()[1].split('/')[0],port)
                          flag = 1
                          break
              os.remove('temp.txt') 

          # error message incase temp.text couldnot be created.    
          else:
              print('Permission Denied!')

    return flag

# variable to mark recieving mode.
xflag = 0

# Flag is set to 1 if sharing is successful.
flag = 0

### html program to recieve files ###
html='''
<html>
<body>
   <h1> Leaky-LAN Web Portal </h1>
   <form enctype = "multipart/form-data" action = "cgi-bin/action.py" method = "post">
   <p>Enter File: <input type = "file"name ="filename" /></p>
   <p>Confirm Upload: <input type = "submit" value = "Submit" /></p>
   <br>
   <p> Developed by M.Anish [aneesh25861@gmail.com] </p>
</form>
</body>
</html>
'''
### End of html program

### Cgi program ###
action='''#!/usr/bin/python3
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   out=open('files/' + fn, 'wb')
   out.write(fileitem.file.read())
'''
### End of cgi program ###
 
# function to recieve files
def recieve():

    # set xflag to mark recieving mode.
    xflag = 1

    # start copying required files to recieve files.
    if os.path.exists("files") is False:
        os.mkdir("files")
        os.mkdir("cgi-bin")
        print("All your recieved files will be stored at " + os.getcwd() + "/files")

    if os.path.exists("cgi-bin"):
        os.chdir("cgi-bin")
        with open("action.py","w") as f:
            f.write(action)
        os.chdir('..')
        if platform.system().lower()!="windows":
            os.chdir("cgi-bin")
            os.system("chmod +x action.py")
            os.chdir('..')

    if os.path.exists("index.html") is False:
        with open("index.html","w") as f:
            f.write(html)

    flag = getip(':9000')
    
    # Recieving mode.
    if xflag == 1 and flag == 1:

        # start python http.server at default port 8000 in cgi mode
        os.system('py -m http.server 9000 --cgi' if platform.system().lower() == 'windows' else 'python3 -m http.server 9000 --cgi')
    
    # Throw error if ipv4 address couldnot be obtained.    
    else:
        print("It seems Your Device is NOT connected to any Network !")

def serve():
    # To get Folder whose files are to be shared. 
    folder = input('Enter Folder name:')

    # To check if folder entered by user is valid or not.
    try:
        os.chdir(folder)
    except Exception as e:
        print('Folder Not Found :(')
        choice = input("\nDo you want to share "+ os.getcwd()  + " in the local network ? (yes/no)\n=>>")
        print()
        if choice.lower() != "yes":
           sys.exit()

    flag = getip()

    # If getting an ipv4 address for sharing successful start server.
    if flag == 1:

        # Remove index html files which might interfere while running http server.
        if os.path.exists("index.html"):
            os.remove("index.html")

        # start python http.server at default port 8000
        os.system('py -m http.server ' if platform.system().lower() == 'windows' else 'python3 -m http.server')
    
    # Throw error if ipv4 address couldnot be obtained.    
    else:
        print("It seems Your Device is NOT connected to any Network !")


# menu
def menu():
    
    print(" Menu :-")
    print("\n 1) Share Files \n 2) Recieve Files")
    ch = input("\nEnter choice:")
    while 1:
        if ch not in ('1','2','c','close','exit'):
            print("\n\ainvalid choice selected!\n")
            ch = input("\n Enter choice:")
        else:
            break

    if ch == '2':
        
        recieve()

        # To clear screen.
        os.system('cls' if platform.system().lower() == 'windows' else 'clear')
        menu()

    elif ch in ('c','close','exit'):
        sys.exit()

    else:
        serve()

menu()


