# Leaky-LAN

### [ Note ] : This project is no longer maintained , it is advised not to use this software anymore , This project was developed with minimal dependencies in mind however since python 3.13 removes many standard libraries used in this project as mentioned in [PEP594](https://peps.python.org/pep-0594/#cgi) we have decided to sunset this project. Users are advised to use [Magic-Wormhole](https://github.com/magic-wormhole/magic-wormhole) or [Onion Share](https://github.com/onionshare/onionshare) instead. Huge thanks to all contributors for their hard work.

It is a simple file sharing and HTTP server in LAN for windows and Linux systems which have python3 installed. Allows files to be shared in an easy and accessible way through LAN. No file sharing service is needed!

![start](https://github.com/Sam6900/Leaky-LAN/assets/85671637/29d96436-549b-48a5-9814-2b0466fd5cce)

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

 ![receive](https://github.com/Sam6900/Leaky-LAN/assets/85671637/0fba9560-9e43-4969-9109-6f8634e9c59c)

 From this interface, you can choose a file and have it instantly uploaded to be shared. 
 Various file sizes are supported.
 
 - Interface to Share Files from computer : -
 
![send](https://github.com/Sam6900/Leaky-LAN/assets/85671637/8c10de40-fcaa-4460-a5cb-28752063b31e)

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
For contributing to this project refer [CONTRIBUTING.md](/CONTRIBUTING.md) file.
