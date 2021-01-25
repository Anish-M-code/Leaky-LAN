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

import os
import platform

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
folder = input('Enter Folder name:')

try:
  os.chdir(folder)
except Exception as e:
   print('Folder Not Found :(')

if platform.system().lower() == 'windows':
  os.system('ipconfig >temp.txt')
  if os.path.exists('temp.txt'):
    with open('temp.txt') as f:
           for x in f:
                 if 'IPv4' in x:
                     print('Enter in Browser :',x.split()[-1],':8000')
                     break
    os.remove('temp.txt')                       
  else:
    print('Permission Denied!')
else:
  os.system('ip a >temp.txt')
  if os.path.exists('temp.txt'):
    with open('temp.txt') as f:
           for x in f:
                 if ('inet ' in x) and ('127.0.0.1' not in x):
                     print('Enter in Browser :',x.split()[1].split('/')[0],':8000')
                     break
    os.remove('temp.txt') 
  else:
    print('Permission Denied!')
os.system('py -m http.server' if platform.system().lower() == 'windows' else 'python3 -m http.server')

