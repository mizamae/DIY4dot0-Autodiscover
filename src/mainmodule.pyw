#!/usr/bin/env python
'''
Created on 3 nov. 2019

@author: Zabaleta-De Carlos
'''
def getMyIP():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.0.0.8', 1027))
    except socket.error:
        return None
    return s.getsockname()[0]

def checkIP(IP):
    import requests
    try:
        r=requests.get('http://'+IP+'/diy4dot0autodiscoverprobe',timeout=0.2)
        if r.status_code==204:
            return True
        else:
            return False
    except: # normally timeout
        return False

def findMyServer ():  
    IP=getMyIP()
    IPdigits=IP.split('.')
    label2 = tk.Label(root, text= 'Trying ', fg='black', font=('helvetica', 10))
    label2.pack(side='left')
    #canvas1.create_window(150, 250, window=label2)
    for value in range(150,255):
        if value != int(IPdigits[-1]):
            address=IPdigits[0]+'.'+IPdigits[1]+'.'+IPdigits[2]+'.'+str(value)
            label2.configure(text='Trying '+address)
            root.update()
            found=checkIP(IP=address)
            if found:
                label2.configure(text='')
                root.update()   
                label1 = tk.Label(root, text= 'Found server at '+address, fg='green', font=('helvetica', 12, 'bold'))
                #canvas1.create_window(150, 200, window=label1)
                label1.pack(side='left')
                #from time import sleep
                #sleep(1)
                webbrowser.open("http://"+address)
                root.destroy()
                break
    if not found:
        label1 = tk.Label(root, text= 'Server not found', fg='red', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 200, window=label1)

import tkinter as tk
import webbrowser
import os

root= tk.Tk()
root.title("Autodiscovering tool for DIY4dot0")
background_image=tk.PhotoImage(file="C:\\Users\\Zabaleta-De Carlos\\Documents\\GitHub\\DIY4dot0-AutoDiscover\\src\\dist\\media\\Home_40.gif")
                                # os.path.join('media','Home_40.gif'))
                               #"C:\\Users\\Zabaleta-De Carlos\\Documents\\GitHub\\DIY4dot0-AutoDiscover\\src\\dist\\media\\Home_40.gif")

canvas1 = tk.Canvas(root, width = 1000, height = 300)
canvas1.pack(expand='no', fill='both')
canvas1.create_image(0, 0, image=background_image, anchor='nw')

button1 = tk.Button(text='Find my server',command=findMyServer, bg='green',fg='white',anchor='sw')
button1.pack(side='left')

label3 = tk.Label(root, text= 'by Mikel Zabaleta', fg='black', font=('helvetica', 8))
label3.pack(side='right')

root.mainloop()
