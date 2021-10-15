import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia import exceptions

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()
 
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring sir")

    elif hour>=12 and hour<18:
        speak("Good Afernoon sir")
    else:
        speak("Good Evening sir")

    speak("I am Friday . How can i help you")

def takecomand():
    #TAkes input from user and return sring

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in' )
        print(f"User said:{query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"     
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('atul.sonkamble4321@gmail.com, Manthan@1234')
    server.sendmail('atul.sonkamble4321@gmail.com',to , content)
    server.close()
         
if __name__ == '__main__':
    wishme()
    while True:
        query=takecomand().lower()

        if 'wikipedia' in query:
            if wikipedia != query:
                speak("Can't find try again")
            else:
                speak("Searching wikipedia")
                query=query.replace("wikipedia","")
                resullts= wikipedia.summary(query, sentences=2)
                print(resullts)
                speak(resullts)
            


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir='D:\\radaa'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")
            print(strtime)
        
        elif 'open code' in query:
            pyPath="C:\\Users\\atuls\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(pyPath)
        
        elif 'email to atul' in query:
            try:
                speak("What should i say")
                content=takecomand()
                to = "supritsalvi@gmail.com"
                sendEmail=(to , content)
                speak("Email has been send successfully")
            except Exception as e:
                print(e)
                print("Sorry sir can't send email")
        
        elif 'thank you for your help' in query:
            speak("see you soon sir")
            quit()

        elif 'how are you' in query:
            speak("I am fine thankyou")
        
            

                



