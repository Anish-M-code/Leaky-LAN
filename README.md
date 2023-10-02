# Leaky-LAN

It is a simple file sharing and HTTP server in LAN for windows and Linux systems which have python3 installed. Allows files to be shared in an easy and accessible way through LAN. No file sharing service is needed!

<img src="https://github.com/Anish-M-code/Leaky-LAN/raw/master/screenshot.png">

Note: Files shared using this tool is available to each and every device 
 connected to LAN. Don't use on public Networks!
 
 ## Main Features
 
 - Easy to use, setup, and maintain
 - 100% Open source
 - Setup required only on one computer.
 - Bidirectional sharing of files possible using new web interface.

When LeakyLAN loads up, you are prompted to choose 1 or 2.
1 allows the service to share files from the computer.
2 allows the service to receive files to the user's computer.

 
 ## Web Interfaces
 
 - Interface to Recieve Files to computer : -
 
 <img src="https://github.com/Anish-M-code/Leaky-LAN/raw/master/webinterface2.png">

 From this interface, you can choose a file and have it instantly uploaded to be shared. 
 Various file sizes are supported.
 
 - Interface to Share Files from computer : -
 
 <img src="https://github.com/Anish-M-code/Leaky-LAN/raw/master/webinterface.png">

 From this interface, you can choose which folder has the file you want shared.
 The folder will be shared over LAN to each device that is connected.

 
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

Press Ctrl and C both at same time to terminate LeakyLan.

## Contributing
1. Fork the repository
2. Clone your fork
```bash
git clone htpps://github.com/<username>/Leaky-LAN.git
```
3. Go to the project directory
```bash
cd Leaky-LAN
```
4. Follow the installation instructions above
5. Submit pull request
