# coded by : bachir bouguelmouna
# to demonstrate how to code about window with: 'timer' and 'transparent' and 'images'
# this code it's a part 'snipet' of program that i developed 'Gestion des clients MT/MP/FSM'
# you can see that i imported 'socket' and 'os' and 'platform' to get sys info

from Tkinter import *

import time 
from PIL import Image ,ImageTk
root=Tk()
root['background']='azure4'

about_img = ImageTk.PhotoImage(Image.open('about_img.png'))
about_img1 = ImageTk.PhotoImage(Image.open('ok.png'))

def about_fen():
        import socket
        import platform
        import os
        global about_img
        about =Toplevel(bd=8) 
        about["bg"] = "black"
        screen_width = root.winfo_screenwidth() # to center the window
        screen_height = root.winfo_screenheight() # to center the window
        xx = (screen_width/2) - (200) # to center the window
        yy = (screen_height/2) - (150) # to center the window
        about.geometry('%dx%d+%d+%d' % (450, 300, xx, yy))
        about.overrideredirect(1) # window like splash screen
        about.attributes('-alpha', 0.8) # activate transparent with 80%
        about_frame=LabelFrame(about, text="About  ",bg='black',bd=10,fg='purple3',font=("Trebuchet MS", 12,'bold'))
        about_frame.pack(fill=BOTH,expand=YES)
        about_logo = Label(about_frame,image = about_img)
        about_logo.place(x = 20, y = 25)
        about_label = Label(about_frame,text=" Gestion Dés Clients   V 1.0",font=("Trebuchet MS", 13,'bold'),bg='black',fg='white')
        about_label.place(x = 32, y = 34)
        about_label1 = Label(about_frame,text="Developed by : Agence Commerciale Metlili 2017",font=("Trebuchet MS", 11,'bold','italic'),bg='black',fg='purple3')
        about_label1.place(x = 15, y = 80)
        about_label2 = Label(about_frame,text="Current Session is: "+(os.environ['HOME']),font=("Trebuchet MS", 9,'bold','italic'),bg='black',fg='white')
        about_label2.place(x = 15, y = 105)
        about_label3 = Label(about_frame,text="Your systeme is: "+platform.platform(),font=("Trebuchet MS", 9,'bold','italic'),bg='black',fg='white')
        about_label3.place(x = 15, y = 125)
        about_label4 = Label(about_frame,text="Your Adress IP is: "+socket.gethostbyname(socket.gethostname()),font=("Trebuchet MS", 9,'bold','italic'),bg='black',fg='white')
        about_label4.place(x = 15, y = 145)
        about_label5 = Label(about_frame,text="Your CPU is: "+platform.processor(),font=("Trebuchet MS", 9,'bold','italic'),bg='black',fg='white')
        about_label5.place(x = 15, y = 165)
        about_ok = Label(about_frame,image = about_img1,bg='black')
        about_ok.place(x = 150, y = 200)
        Label_ok = Label(about_frame,text='OK',bg='black',fg='white',font=("Trebuchet MS", 11,'bold','italic'))
        Label_ok.place(x = 180, y = 207)
        about.after(4500,about.destroy)

about_btn=Button(root,text='About..',width=20,font=("Trebuchet MS", 11,'bold','italic'),bg='black',bd=10,fg='purple3',command=about_fen).pack(padx=10,pady=10)
exit_btn=Button(root,text='Exit..',width=20,font=("Trebuchet MS", 11,'bold','italic'),bg='black',bd=10,fg='purple3',command=root.destroy).pack(padx=10,pady=2)
root.mainloop()        
