
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
A simple file sharing service using python http.server 
developed by M.Anish <aneesh25861@gmail.com>

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

# Flag is set to 1 if sharing is successful.
flag = 0

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
                                print('Enter in Browser :',buff[x].split()[-1],':8000')
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
                      print('Enter in Browser :',x.split()[1].split('/')[0],':8000')
                      flag = 1
                      break
          os.remove('temp.txt') 

      # error message incase temp.text couldnot be created.    
      else:
          print('Permission Denied!')

# If getting an ipv4 address for sharing successful start server.
if flag == 1:

    # start python http.server at default port 8000
    os.system('py -m http.server ' if platform.system().lower() == 'windows' else 'python3 -m http.server')

# Throw error if ipv4 address couldnot be obtained.    
else:
    print("It seems Your Device is NOT connected to any Network !")


