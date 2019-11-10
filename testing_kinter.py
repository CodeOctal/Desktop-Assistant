"""        
        self.label0 = tk.Label(self.root, text='-------DO YOU WANT YOUR CHAT HISTORY-------',bg='cyan',bd='10px',relief=tk.RAISED,font=("Courier", 15))
        self.label0.grid(row=2, column=1, columnspan=2,rowspan=2,padx=40, pady=40)
        
        self.button2 = tk.Button(self.root,command=self.backup,text='YES',bg='cyan',relief=tk.RAISED,font=("Courier", 15))
        self.button2.grid(sticky=tk.W,row=4,column=1,pady=10,padx=180)
        
        self.button3 = tk.Button(self.root,command=self.popupmsg,text='NO',bg='cyan',relief=tk.RAISED,font=("Courier", 15))
        self.button3.grid(sticky=tk.E,row=4,column=1,padx=180)
        self.root.mainloop()   
"""







#from gtts import gTTS
import speech_recognition as sr
import os
#import threading
import sys
import re
import webbrowser
import smtplib
import requests
#import subprocess
from pyowm import OWM
import ctypes
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import wolframalpha
fromaddr = "aishwarya.raman96@gmail.com"
toaddr = "aishwarya.raman96@gmail.com"

#import youtube_dl
#import vlc
#import urllib.request
#import urllib2
#import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import urllib.request
import wikipedia
#import random
from time import strftime
import pyttsx3
engine = pyttsx3.init()
import win32com.client as wincl
import tkinter as tk
from tkinter import ttk
f=open("testing.txt","w")

NORM_FONT = ("Helvetica", 10)
class Widget():
    def __init__(self):
        #super().__init__(parent)
        self.root = tk.Tk()
        self.root.title('personal assistant')
        self.root.resizable(90, 90)
        self.root.geometry('550x650')
        self.root.configure(background= '#1d1a75')
       
        self.root.iconbitmap('women.ico')
        
        
        
        
        
        engine.say("Hi User, I am Sofia and I am your personal voice assistant, Please give a command or say help me and I will tell you what all I can do for you.")

        try :
            urllib.request.urlopen("https://www.google.co.in")
            engine.say("You are connected to internet")
            
            

        except:
            engine.say("it seems you are not connected to the internet")
            engine.say("I can provide you with the ofline facilties like chnage wallpaper,launching appliications and opening up folders")
           
        
        engine.runAndWait()
        
       #self.label1 = tk.Label(self.root, text='CLICK ME AND IAM AT YOUR SERVICE',bg='cyan',bd='10px',relief=tk.RAISED,font=("Courier", 20))
        #self.label1.grid(row=0, column=1, padx=40, pady=40)
        #self.entry = tk.Entry(self.root)
        #self.entry.pack()
        self.root.iconbitmap('women.ico')

        
        photo = tk.PhotoImage(file ='womenb.png')

        self.button1 = tk.Button(self.root, image=photo, command=self.clicked1,relief=tk.FLAT)
        self.button1.grid(row=1, column=1, padx=20, pady=20)
        self.root.update()
        self.button2 = tk.Button(self.root,command=self.popupmsg,text='EXIT',bg='#e6eaeb',relief=tk.RAISED,font=('Helvetica  25  bold'))
        self.button2.grid(row=4,column=1,pady=10,padx=180)
        
        
        
        
        #self.button = tk.Button(self.root, text='Speak!', command=self.clicked)
        #self.button.pack()
        #while True:
        
        #self.btn = tk.Button(self.root, text='replicate',command = self.speaking)
        #self.btn.pack()
     
        
        self.root.mainloop()   
#buttons for chat--------------------------------------------------------------------------------------------------------------------------------------------------------


    
    def clicked1(self):
        engine.say("please speak")
        engine.runAndWait()
        self.assistant(self.speaking())
        
          
    def filetext(self,command):
        if command:
            f.write('user ->' + command + '\n')

    def sofia(self,command):
        if command:
            f.write('sofia ->' + command + '\n')
            f.write('--------------\n')
            
    
    
  
   

         #startfile('C:/Users/AISHU/Desktop/2ND YEAR PROJECT MCA/desktopAssistant-master/testing.txt') 
        
        
    
    def popupmsg(self):
        self.popup = tk.Tk()
        self.popup.title('personal assistant')
        self.popup.resizable(90, 90)
        #self.popup.geometry('400x400')
        self.popup.configure(background='#1d1a75')
        self.popup.iconbitmap('women.ico')
        
        self.label = ttk.Label(self.popup, text=" DO YOU WISH TO HAVE CHAT BACKUP ",background='#e6eaeb',font=('Helvetica  20  bold'))
        self.label.grid(pady=10)
        
        self.button3 = tk.Button(self.popup,command=self.yes,text='YES',bg='#e6eaeb',relief=tk.RAISED,font=('Helvetica  15  bold'))
        self.button3.grid(sticky=tk.W,padx=80,pady=10,row=1,column=0)
        
        self.button4 = tk.Button(self.popup,command=self.no,text='CLOSE',bg='#e6eaeb',relief=tk.RAISED,font=('Helvetica  15  bold'))
        self.button4.grid(sticky=tk.E,padx=80,pady=10,row=1,column=0)
        
        #B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        #B1.pack()
        self.popup.mainloop()
    
        
    def yes(self):
         
       # if sys.exit():
       
      
       self.root.destroy()
       self.popup.destroy()
       os.startfile("C:Users/AISHU/Desktop/2ND YEAR PROJECT MCA/desktopAssistant-master/testing.txt")
        #self.config = Config(self)
        
        
        
        
     
    def no(self): 
     
       # self.root.destroy()
        #self.popup.destroy()
        self.pop = tk.Tk()
        self.pop.title('personal assistant')
        self.pop.resizable(90, 90)
     
        self.pop.configure(background='black')
        self.pop.iconbitmap('women.ico')
        
        self.label5 = tk.Label(self.pop, text=" THANK YOU ",background='cyan',foreground='white',relief=tk.RAISED,font=('Helvetica  15  bold'))
        self.label5.grid()
      
        self.root.destroy()
        self.popup.destroy()
        
        self.pop.mainloop()
        
       
   
        #self.root.destroy()
    
    
    def sofiaResponse(self,audio):
        "speaks audio passed as argument"
        print(audio)

        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(audio)

        
    def speaking(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print ('Say Something!')
        
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            print ('Done!')
            
        
        try:
            command = r.recognize_google(audio).lower()
            
            print('You said: ' + command + '\n')
            #self.labelb = tk.Label(self.root, text='You said: ')
            #self.labelb.grid(row=3, column=4, padx=40, pady=40)
            
            
            self.filetext(command)
            
          
        except sr.UnknownValueError:
            print('....')  
          #  self.label5 = tk.Label(self.root, text='....')
           # self.label5.pack()
                        
            command=self.speaking();
        print('returning')
        return command
    
        
    
    
    
    
    
    
    
    def assistant(self,command):
        
        #open subreddit Reddit
        if 'open reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
                webbrowser.open(url)
                self.sofiaResponse('The Reddit content has been opened for you Sir.')
                self.sofia('The Reddit content has been opened for you Sir.')
                self.sofia(url)
        elif 'shutdown' in command or 'bye' in command or 'tata' in command :
            self.sofiaResponse('Bye bye. Have a nice day')
            self.sofia('Bye bye. Have a nice day')
            
            
            sys.exit()
            
        
        
        
        elif 'open website' in command:
            reg_ex = re.search('open website (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                
            
                url = 'https://www.' + domain  + '.com' 
                webbrowser.open(url)
                self.sofiaResponse('website ' + url + ' is opened')
                self.sofia('website' + url + 'is opened')
                #self.label6 = tk.Label(self.root, text='website' + url + 'is opened')
                #self.label6.grid()
            else:
                pass
       
    # wait until thread 1 is completely executed 
        elif 'play youtube video for' in command:
            reg_ex = re.search('youtube (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.youtube.com/results?search_query=' + domain
                webbrowser.open(url)
                self.sofiaResponse('The youtube videos are available.')
                
                self.sofia('The youtube videos are available.' + url)
                #self.label6a = tk.Label(self.root, text='The youtube videos are available.' + url)
                #self.label6a.grid()
                
            else:
                pass
 #google search
  
    
        elif 'google' in command or 'please google' in command:                                                           #what happens when google keyword is recognized
            reg_ex = re.search('google (.+)', command)
            words = command.split()
            del words[0:1]
            st = ' '.join(words)
            print('Google Results for: '+ str(st))
            url='http://google.com/search?q='+ st
            webbrowser.open(url)
            self.sofiaResponse('Google Results for: '+str(st))
           
            self.sofia('Google Results for: '+str(st) + url)
 
#greetings
        elif 'hello' in command or 'hey' in command:
            day_time = int(strftime('%H'))
            if day_time < 12:
                self.sofiaResponse('Hello ASH. Good morning')
                self.sofia('Hello ASH. Good morning')
            elif 12 <= day_time < 18:
                self.sofiaResponse('Hello ASH. Good afternoon')
                self.sofia('Hello ASH. Good afternoon')
            else:
                self.sofiaResponse('Hello ASH. Good evening')
                self.sofia('Hello ASH. Good evening')

         
#joke
        elif 'joke' in command:
            res = requests.get(
                'https://icanhazdadjoke.com/',
            headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                self.sofiaResponse(str(res.json()['joke']))
                self.sofia(str(res.json()['joke']))
            else:
                self.sofiaResponse('oops!I ran out of jokes')
                self.sofia('oops!I ran out of jokes')

#top stories from google news
        elif 'news for today' in command or 'news' in command:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
            
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:3]:
                    self.sofiaResponse(news.title.text.encode('utf-8')) 
                    self.sofia(news.title.text)
            except Exception as e:
                print(e)

#current weather
        elif 'current weather' in command or 'weather' in command:
            reg_ex = re.search('current weather in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                self.sofiaResponse('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
                self.sofia('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
#time
        elif 'time' in command:
            import datetime
            now = datetime.datetime.now()
            self.sofiaResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))
            self.sofia('Current time is %d hours %d minutes' % (now.hour, now.minute))

 #email  
        elif 'please email' in command:
            self.sofiaResponse('Who is the recipient?')
            recipient = self.myCommand()
            if 'ash' in recipient:
                msg = MIMEMultipart() 
  
# storing the senders email address   
                msg['From'] = fromaddr 
  
# storing the receivers email address  
                msg['To'] = toaddr 
  
# storing the subject  
                msg['Subject'] = "hello"
  
# string to store the body of the mail 
                body = "Body_of_the_mail"
  
# attach the body with the msg instance 
                msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
                filename = "final forward.pdf"
                attachment = open("C:/Users/AISHU/Desktop/final forward.pdf", "rb") 
  
# instance of MIMEBase and named as p 
                p = MIMEBase('application', 'octet-stream') 
  
# To change     the payload into encoded form 
                p.set_payload((attachment).read()) 
  
# encode into base64 
                encoders.encode_base64(p) 
   
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
                msg.attach(p) 
  
# creates SMTP session 
                s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
                s.starttls() 
  
        # Authentication 
                s.login(fromaddr,"xyfsfvqsgawkfhjh") 
  
        # Converts the Multipart msg into a string 
                text = msg.as_string() 
  
        # sending the mail 
                s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
                s.quit() 
                self.sofiaResponse('Email has been sent successfuly. You can check your inbox.')
                self.sofia('Email has been sent successfuly. You can check your inbox.')
            else:
                self.sofiaResponse('I don\'t know what you mean!')
                self.sofia('I don\'t know what you mean!')



#launch any folder
        elif 'from desktop view folder ' in command or 'view folder' in command:
            reg_ex = re.search('from desktop view folder (.*)', command)
            if reg_ex:
                appname = reg_ex.group(1)
            
                appname1 = appname 
            #subprocess.call(["open", "-n", "/C:\/" + appname1], stdout=subprocess.PIPE)
                os.startfile('C:/Users/AISHU/Desktop/' + appname1)
            #subprocess.call()
        
            
                self.sofiaResponse('I have launched the desired application')
                self.sofia('I have launched the desired application')
#calculation
        elif 'calculate' in command:
            reg_ex = re.search('calculate (.*)', command)
            app_id = "AUXH6Q-LA7AA5J66V" 
            client = wolframalpha.Client(app_id) 
  
            indx = command.lower().split().index('calculate') 
            query = command.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            self.sofiaResponse("The answer is " + answer) 
            self.sofia("The answer is " + answer)
            
            
        elif 'thank you' in command or 'thanks' in command:
            self.sofiaResponse('your welcome')
            self.sofia('your welcome')
    
        elif 'help me' in command:
            self.sofiaResponse("""
       
        You can use these commands and I'll help you out:
        1-. Open reddit subreddit 
        2.  Open website
        3.  play youtube video for
        4.  please google
        5.  from desktop view folder
        6.  news for today
        7.  Joke
        8.  Send email/email
        9.  Current weather in {cityname} 
        10. change wallpaper
        11. Time
        12. tell me about xyz 
        13. Calculate
        14  where is {location}
        15. launch app
        """)    
            
            
            
#wallpaper
        elif 'change wallpaper' in command:
            reg_ex = re.search('change wallpaper (.*)', command)
            path_user = os.path.expanduser('~')
            if reg_ex:
                appname = reg_ex.group(1)
            
                appname1 = appname +'.jpg'
        

        #name_of_file = 'img.jpg'
                path_to_file = os.path.join(path_user,'Desktop','wallpaper',appname1)
                print(path_to_file) # this print C:\Users\Sebastian\Desktop\wallpapers\vRATOkv.jpg 
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)                    
                self.sofiaResponse('I have changed the desired wallpaper')
                self.sofia('I have changed the desired wallpaper')
#launch any app
        elif 'launch app' in command:
            reg_ex = re.search('launch app (.*)', command)
            if reg_ex:
                appname = reg_ex.group(1)
            
                appname1 = appname + ".lnk"
            #subprocess.call(["open", "-n", "/C:\/" + appname1], stdout=subprocess.PIPE)
            
                os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/' + appname1)
            #subprocess.call()
        
            
                self.sofiaResponse('I have launched the desired application')
                self.sofia('I have launched the desired application')
            
            
#meanings                        
        elif 'tell me about' in command:
            reg_ex = re.search('tell me about (.*)', command)
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                self.sofiaResponse(ny.content[:500].encode('utf-8'))
                self.sofia(ny.content[:500].encode('utf-8'))
                
                
              
            
#location
        elif "where is" in command:
            reg_ex = re.search('where is (.*)', command)
            command = command.split(" ")
            location = command[2]
            self.sofiaResponse("Hold on ASH, I will show you where " + location + " is.")
        
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
            self.sofia("Hold on ASH, I will show you where " + location + " is." + "https://www.google.nl/maps/place/" + location + "/&amp;" )
        
        else:
            self.sofiaResponse('sorry i dont understand please rephrase your sentence')
            self.sofia('sorry i dont understand please rephrase your sentence')
 
if __name__ == '__main__':
    widget = Widget()