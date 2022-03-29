# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:23:58 2021

@author: 91703
"""
import screen
import anim
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import time
from win10toast import ToastNotifier
import webbrowser

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

class Widget:
    def __init__(self):
        
        root = Tk()
        root.title('PIEDPIPER')
        root.geometry('920x620')
        root.configure(background='#090e38')
        #root.attributes('-alpha',0.5)

        
        imggg = PhotoImage(file="2.png")
        label = Label(root,image=imggg)
        label.place(relx=0, rely=0,relheight=1,relwidth=1)
        
        
     
        #root.colspan="3"
        """frame=Frame(root,bg="#090e38")
        frame.place(relx=0,rely=0,relheight=0.2,relwidth=0.2)
        img = ImageTk.PhotoImage(Image.open('ic.ico'))
        panel = Label(root,bg="#090e38",image=img)
        panel.place(relx=0.1,rely=0,relheight=0.15,relwidth=0.1)"""
        
        label=Label(root,text="PIEDPIPER",
                    font=("Times New Roman",40),bg="#030927",fg="white")
        label.place(relx=0.45,rely=0,relheight=0.1,relwidth=0.7)
        """text = Text(root,height=10,width=53)
        text.place(relx=0.4, rely=0,relheight=0.1,relwidth=0.2)
        button = Button(root,text='SEND',relief=RAISED,font=('Arial Bold', 18))
        button.place(relx=0.4,rely=0,relheight=0.2,relwidth=0.2)"""

        #imgg=anim.ImageLabel( ImageTk.PhotoImage(anim.ImageLabel.load('lena.jpg')))
        frame=Frame(root,bg="#030927")
        frame.place(relx=0,rely=0,relheight=0.64,relwidth=0.64)
        imgg = ImageTk.PhotoImage(Image.open('3.png'))
        panel = Label(frame, image=imgg)
        panel.pack()
        
        
        
        
        """frame=Frame(root,bg="#090e38")
        frame.place(relx=0,rely=0.62,relheight=0.4,relwidth=0.9)
        #img = ImageTk.PhotoImage(Image.open('e.jpg'))
        #Jarvis command
        button=Button(frame,text="Jarvis",bg="white",fg="black",font=("Times New Roman",15),
                      command=lambda:self.clicked())
        button.place(relx=0.1,rely=0.1,relheight=0.15,relwidth=0.15)
        changeOnHover(button, "red", "white")
        
        button=Button(frame,text="Close",bg="white",fg="black",font=("Times New Roman",15),
                      command=root.destroy)
        button.place(relx=0.3,rely=0.1,relheight=0.15,relwidth=0.15)
        changeOnHover(button, "red", "white")
        
        button=Button(frame,text="Perks",bg="white",fg="black",font=("Times New Roman",15),
                      command=lambda:self.perks())
        button.place(relx=0.65,rely=0.1,relheight=0.15,relwidth=0.15)
        changeOnHover(button, "red", "white")
        
        button=Button(frame,text="Help ?",bg="white",fg="black",font=("Times New Roman",15),
                      command=lambda:self.hel())
        button.place(relx=0.85,rely=0.1,relheight=0.15,relwidth=0.15)
        changeOnHover(button, "red", "white")"""
        
        label=Label(root,text="VOICE ASSISTANT",
                    font=("Times New Roman",30),bg="#030927",fg="white")
        label.place(relx=0,rely=0.66,relheight=0.1,relwidth=0.64)
        
        frame2=Frame(root,bg="#030927")
        frame2.place(relx=0,rely=0.75,relheight=0.64,relwidth=0.64)
        button=Button(frame2,text="JARVIS",bg="white",fg="black",
                      command=lambda:self.jarvis(),font=("Times New Roman",11))
        button.place(relx=0.2,rely=0.1,relheight=0.1,relwidth=0.3)
        changeOnHover(button, "red", "white")
        
        button=Button(frame2,text="WEBSITE",bg="white",fg="black",
                      command=lambda:self.balanced(),font=("Times New Roman",11))
        button.place(relx=0.6,rely=0.1,relheight=0.1,relwidth=0.3)
        changeOnHover(button, "red", "white")
        
        label=Label(root,text="CRM SYSTEM",
                    font=("Times New Roman",20),bg="#030927",fg="white")
        label.place(relx=0,rely=0.9,relheight=0.1,relwidth=0.64)
        
        
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.4,relheight=0.4,relwidth=0.4)
        label = Label(text="\"DASHBOARD\"\n\n 1.Trigger Xmas mails\n 2.Generate Coupons",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        
        """frame1=Frame(root,bg="white")
        frame1.place(relx=0,rely=0.75,relheight=0,relwidth=1)"""
        
        #frame1=Frame(root,bg="white")
        #frame1.place(relx=0,rely=0.98,relheight=0,relwidth=1)
        
        frame1=Frame(root,bg="#030927")
        frame1.place(relx=0.7,rely=0.45,relheight=0.6,relwidth=0.3)
        button=Button(frame1,text="BALANCED",bg="white",fg="black",
                      command=lambda:self.balanced(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.1,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="PINCH PENNY",bg="white",fg="black",
                      command=lambda:self.pinchpenny(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.2,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="NORMAL",bg="white",fg="black",
                      command=lambda:self.normal(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.3,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SPENDERS",bg="white",fg="black",
                      command=lambda:self.spenders(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.4,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="TARGET",bg="white",fg="black",
                      command=lambda:self.stack(),font=("Times New Roman",10))
        button.place(relx=0.01,rely=0.5,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="EMAIL",bg="white",fg="black",
                      command=lambda:self.mail(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.6,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SMS",bg="white",fg="black",
                      command=lambda:self.sms(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.7,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="TOP CUST",bg="white",fg="black",
                      command=lambda:self.top(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.8,relheight=0.1,relwidth=0.7)
        changeOnHover(button, "red", "white")
        
        """button=Button(frame1,text="SPOTIFY",bg="white",fg="black",
                      command=lambda:self.spot(),font=("Times New Roman",11))
        button.place(relx=0.14,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SHUTDOWN",bg="white",fg="black",
                      command=lambda:self.shut(),font=("Times New Roman",11))
        button.place(relx=0.27,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="WHATSAPP",bg="white",fg="black",
                      command=lambda:self.what(),font=("Times New Roman",11))
        button.place(relx=0.4,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="EDYST",bg="white",fg="black",
                      command=lambda:self.edyst(),font=("Times New Roman",11))
        button.place(relx=0.53,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="TALENTINO",bg="white",fg="black",
                      command=lambda:self.tal(),font=("Times New Roman",11))
        button.place(relx=0.66,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="INDIABIX",bg="white",fg="black",
                      command=lambda:self.bix(),font=("Times New Roman",11))
        button.place(relx=0.79,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="????",bg="white",fg="black",
                      command=lambda:self.bix(),font=("Times New Roman",11))
        button.place(relx=0.92,rely=0.54,relheight=0.3,relwidth=0.1)
        changeOnHover(button, "red", "white")"""
        
        
        
        
       #button=Button(frame,text="Close",bg="white",fg="black",font=("Times New Roman",15))
        #button.place(relx=0,rely=0.7,relheight=0.1,relwidth=0.1)
        #changeOnHover(button, "red", "white")
        
        #button=Button(frame,text="Jarvis",bg="white",fg="black",font=("Times New Roman",15),command=lambda:self.clicked())
        #button.place(relx=0.2,rely=0.1,relheight=0.15,relwidth=0.2)
        #changeOnHover(button, "red", "white")
        #Jarvis('How can i help you Group13?')
        #Jarvis('How can i help you group 13?')
    
        root.iconbitmap('ic.ico')
        root.mainloop() 
        
    def balanced(self):
        
        import balanced
        
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
        
    def pinchpenny(self):
        
        import pinchpenny
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
       
    def normal(self):
        import normal
      
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
       
    def spenders(self):
        import spenders
       
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
       
       
    def target(self):
        import target
       
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
       
    def mail(self):
        import mail
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
       
    def sms(self):
        import sms
        print("***********************************************************")
        frame1=Frame(bg="#030927")
        frame1.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        label = Label(text="SUCCESSFUL",
                      font=("Times New Roman",15,"bold"),bg="#030927",fg="white")
        #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.64,rely=0.1,relheight=0.4,relwidth=0.4)
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
       
    def top(self):
        import top
        print("***********************************************************")
        toaster = ToastNotifier()

        toaster.show_toast("Successful",duration=10,threaded=True)
    
    def jarvis(self):
        import speech_recognition as sr
        import pyttsx3
        import datetime
        import time
        import subprocess
        import requests
        from gtts import gTTS
        import playsound
        from time import sleep
        import threading
        import speech_recognition as sr
        import pyttsx3
        import datetime
        import wikipedia
        import webbrowser
        import os
        import time
        import subprocess
        from PIL import Image,ImageTk
        from tkinter import ttk
        import wolframalpha
        import json
        import requests
        from covid_india import states
        from gtts import gTTS
        import random
        import playsound
        import datetime
        import ecapture
        import pyjokes
        import pywhatkit as py
        import pyautogui
        from time import sleep
        from urllib.request import urlopen
        
        
        
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        
        def Jarvis(text):
            engine.say(text)
            engine.runAndWait()
            print(text)
        
        def wishMe():
            hour=datetime.datetime.now().hour
            if hour>=0 and hour<12:
                Jarvis("Hello,Good Morning, How can I help you today")
                print("**************************")
                #print("Hello,Good Morning")
            elif hour>=12 and hour<18:
                Jarvis("Hello,Good Afternoon, How can I help you today")
                print("**************************")
                #print("Hello,Good Afternoon")
            else:
                Jarvis("Hello,Good Evening, How can I help you today")
                print("**************************")
                #print("Hello,Good Evening")
        
        def takecommand():
            r=sr.Recognizer()
            r.dynamic_energy_threshold = False
            #r.energy_threshold = 3000
            
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
                statement=''
                
        
                try:
                    statement=r.recognize_google(audio,language='en-in')
                    print(f"User said:{statement}\n")
                    print("**************************")
        
                except Exception as e:
                    Jarvis("Pardon me, please say that again")
                    print("**************************")
                    
                    return "None"
                return statement
            
            
        
            
            
        Jarvis("Loading your AI personal assistant Jarvis")
        print("**************************************************")
        wishMe()
        
        
        Jarvis("Listening...")
        statement = takecommand()
        statement = statement.lower()
        
            
        if "send an email" in statement or "mail" in statement or "send" in statement or "send emails" in statement:
            import spenders
            import target
            import pinchpenny
            import balanced
            import normal
            import top
            import sms
            import mail
            Jarvis("Done with all the emails sir, have a good day")
                
            
        
        
        
            
if __name__== '__main__':
    w= Widget()
time.sleep(1)


