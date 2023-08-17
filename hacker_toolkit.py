
# coding: utf-8
#!/usr/bin/env python
import os
import subprocess
from subprocess import check_call

def intro():
    cmd  = os.system("clear")
    print("""\033[1;32m
-----------------------------------------------------------------------------------------------------------
          
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║   
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║   
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                                                           
                                                                                          Coded By A.dmin
-----------------------------------------------------------------------------------------------------------                                                 
(1) Start Nmap       
(2) Start Nmap graphical (Zenmap)                        
(3) Start Nuclei                            
(4) Start SET  
(5) Start Wireshark                
(6) Start xHydra
(7) Start Armitage
(8) Start SQLmap
(9) Start MSFconsole                               
(10) Start Firefox

(0) Exit
-----------------------------------------------------------------------
""")
    print("\nEnter your choise here :  ")
    var = int(input(""))
    if var == 1 :
        cmd  = os.system("clear")
        print("\nEnter the ip(s) to scan")
        interface = input("")
        print("\nscan start")
        order = "nmap -oN nmap.txt {}".format(interface)
        geny  = os.system(order)
        cmd  = os.system("clear")
        print("\nthe output is in nmap.txt")
        cmd  = os.system("sleep 2")
        intro()
    elif var == 2 :
        print("\nZenmap start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("sudo kaboxer run --component default zenmap --")
        intro()
    elif var == 3 :
        cmd  = os.system("clear")
        print("\nEnter the url to scan")
        interface = input("")
        order = "nuclei -o nuclei.txt -u {}".format(interface)
        geny  = os.system(order)
        cmd  = os.system("clear")
        print("\nthe output is in nuclei.txt")
        cmd  = os.system("sleep 2")
        intro()
    elif var == 4 :
        print("\nSetoolkit start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("sudo setoolkit")
        intro()
    elif var == 5 :
        print("\nwireshark start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("wireshark")
        intro()
    elif var == 0:
        cmd  = os.system("clear")
        print("""\033[1;32m
  /$$$$$$                            /$$ /$$                          
 /$$__  $$                          | $$| $$                          
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$  /$$   /$$  /$$$$$$ 
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$| $$  | $$ /$$__  $$
| $$|_  $$| $$  \ $$| $$  \ $$| $$  | $$| $$  \ $$| $$  | $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$
 \______/  \______/  \______/  \_______/|_______/  \____  $$ \_______/
                                                   /$$  | $$          
                                                  |  $$$$$$/          
                                                   \______/           
""")
        cmd  = os.system("sleep 2")
        exit()
    elif var == 6:
        print("\nxHydra start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("xhydra")
        intro()
    elif var == 7 :
        print("\nArmitage start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("armitage")
        intro()
    elif var == 8 :
        print("\nSQLmap start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("clear")
        cmd  = os.system("sqlmap --wizard")
        intro()
    elif var == 9 :
        print("\nMSFconsole start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("clear")
        cmd  = os.system("msfconsole")
        intro()
    elif var == 10:
        print("\nFirefox start")
        cmd  = os.system("sleep 1")
        cmd  = os.system("firefox")
        intro()
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro()
