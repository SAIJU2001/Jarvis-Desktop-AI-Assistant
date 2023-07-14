import pyttsx3                      #install this module via pip install 
import datetime                     #to access the date and time
import speech_recognition as sr     #for recognition of speech
import wikipedia                    #to access the wikipedia
import webbrowser                   #to access the web browser for search engine
import os                           #a way to interact with the operating system
import smtplib                      #it provides classes for handling the SMTP protocol and sending emails
import random                       #to generate random num



engine = pyttsx3.init('sapi5')              #sapi5 is microsoft speech API(to get the voices)
voices = engine.getProperty('voices')       #inbuild voices are present(you can download your own voice)
# print(voices) using this print command you can check how many voices present in your PC
engine.setProperty('voice',voices[0].id)    #set the first voice present in my PC
# print(voices[0].id) using ths print command you can check who's voice you are uses


#speak function->it is enable to speak any argument
def speak(audio) :
    engine.say(audio)       #engine can speak the audion string
    engine.runAndWait()     #runs an event loop


#greetings for everytime when i run the code
def WishMe() :
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour==12 :
        speak("Good Noon!")
    elif hour>=12 and hour<=17 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")

    speak("I am jarvis sir. Please tell me how may I help you")


def takeCommand() :
#it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening.....")
        r.pause_threshold = 1       #it can pause one sec when you speaking
        audio = r.listen(source)    #listening the source(here source is microphone)

    try :
        print("Recongnizing....")                           #when recognizing ouput screen
        query = r.recognize_google(audio,language='en-in')  #audio recognize and make a english word query and then print that query
        print(f"user said : {query}\n")

    except Exception as e : 
        #print(e) you can print the exception using this command
        print("Say that again Please....")
        return "None"
    return query


def sendEmail(to, content):
    #below 4  lines create an SMTP server instance, connect to the Gmail SMTP server (smtp.gmail.com) on port 587, perform the necessary handshaking (ehlo), and initiate a TLS (Transport Layer Security) encrypted connection (starttls). Then, it logs in to the Gmail account using the provided email address and password.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com', 'your-password')     # enter your mail id and password
    server.sendmail('your@gmail.com', to, content)  #mail has to be send
    server.close()                                      #close the server


#main method
if __name__ == "__main__" : 
    WishMe()
    while True :
        query = takeCommand().lower()
        #logic for executing tasks based on query

        if 'wikipedia' in query :
            speak("Searching Wikipedia.....")               #firstly it is speaking searching wikipedia
            query = query.replace("wikipedia","")
            summary = wikipedia.summary(query)
            sentences = summary.split('. ')                 #sentence split for counting by using '.'
            results = '. '.join(sentences[:2])           #only 2 sentences pick from wikipedia summary 
            speak("According to wikipedia...")               #before speak the reslt this sentence is quite good
            print(results)                        #in the output screen you will see the wikipedia summary also 
            speak(results)                         #speaks the results

        elif 'open youtube' in query :
            #to open the youtube we should open the web browser and search
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            #to open the google we should open the web browser and search
            webbrowser.open("google.com")

        elif 'play music' in query :
            music_dir = 'E:\\Dugga pujor song'      #to get music directory
            songs = os.listdir(music_dir)       #listed all the song present in the directory
            print(songs)
            random_number = random.randint(1, 10)
            os.startfile(os.path.join(music_dir,songs[random_number]))  #start the first song using random anytime any song can play

        elif 'the time' in query :
            #ask jarvis to current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}")

        elif 'open vs code' in query :
            #open the vs code ,below the path of target
            codePath = "C:\\Users\\Saikat Naskar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            #you can create a dictionary (key:name and value:email) for sending the mail
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver@gmail.com" #whom to send   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)    your choice to print the exception or not
                speak("Sorry sir. I am not able to send the email at this moment") 

        elif 'good jarvis' in query or 'great jarvis' in query or 'thank you jarvis' in query :
            #after completing your task if you thank the jarvis
            print("Its my duty sir..Thank you..")
            speak("Its my duty sir..Thank you..")

        elif 'quit' in query :
            print("Thank you sir..I am signing off")
            speak("Thank you sir..I am signing off")
            quit()



    