# Leaky-LAN

It is a simple file sharing and HTTP server in LAN for windows and Linux systems which have python3 installed.

<img src="https://github.com/Anish-M-code/Leaky-LAN/raw/master/screenshot.png">

Note: Files shared using this tool is available to each and every device 
 connected to LAN. Don't use on public Networks!
 
 ## Main Features
 
 - Easy to use , setup and maintain
 - 100% Open source
 - setup required only on one computer.
 - Bidirectional sharing of files possible using new web interface.
 
 ## Web Interfaces
 
 - Interface to Recieve Files to computer : -
 
 <img src="https://github.com/Anish-M-code/Leaky-LAN/raw/master/webinterface.png">
 
 - Interface to Share Files from computer : -
 
 <img src="https://github.com/Anish-M-code/Leaky-LAN/raw/master/webinterface2.png">
 
 Just run it on system which has file to be shared and select the folder.
 The folder will be shared over LAN to each device connected in LAN.
 
 
Quick Installation
------------------

To Install from [PyPI](https://pypi.org/project/leaky-lan/):

Run the following commands in Linux terminal / Windows powershell / command prompt to install :-

```
pip install leakylan
```
Then type the following command to get started :-

```
leakylan
```
To run program by directly downloading from github refer [ Instructions](/Install.md) here.

## FAQ

- <b> Cannot share files in LAN ,why Leakylan doesnot work ? </b>

This must be due to firewall , either apply proper firewall configuration ( recommended ) or disable it temporarily.

- <b> How to stop sharing files ? </b>

Press Ctrl and C both at same time.
