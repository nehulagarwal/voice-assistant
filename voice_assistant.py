import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import pyautogui
import subprocess
import winreg

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 3  #how much time will it take to start recognizing
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

#open anything
app_directories = [
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    os.path.expanduser("~\\AppData\\Local\\Programs"),  # User-specific installations
        "C:\\Windows",                                      # Windows System
    "C:\\Windows\\System32"    ,                         # Windows System32
    os.path.expanduser("~\\AppData\\Local\\WhatsApp"),   # WhatsApp default install location
    os.path.expanduser("~\\AppData\\Roaming\\Telegram Desktop")  # Telegram default install

]


# Helper function to search PATH environment variable
def search_in_path_env(app_name):
    for path in os.getenv("PATH").split(os.pathsep):
        executable_path = os.path.join(path, app_name)
        if os.path.isfile(executable_path):
            return executable_path
    return None

# Helper function to search in Windows Start Menu
def search_in_start_menu(app_name):
    start_menu_paths = [
        os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs'),
        os.path.expandvars(r'%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs')
    ]
    for directory in start_menu_paths:
        for root, dirs, files in os.walk(directory):
            if app_name in files:
                return os.path.join(root, app_name)
    return None

# Helper function to search in Windows Registry
def search_in_registry(app_name):
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths",
        r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\App Paths"
    ]
    for registry_path in registry_paths:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    sub_key_name = winreg.EnumKey(key, i)
                    if app_name.lower() in sub_key_name.lower():
                        with winreg.OpenKey(key, sub_key_name) as sub_key:
                            return winreg.QueryValue(sub_key, None)
        except WindowsError:
            continue
    return None

# Main function to find the application path
def find_application_path(app_name):
    # Add .exe if not provided
    if not app_name.endswith(".exe"):
        app_name += ".exe"
    else:
        app_name = app_name

    # Search in predefined directories
    for directory in app_directories:
        for root, dirs, files in os.walk(directory):
            if app_name in files:
                return os.path.join(root, app_name)

    # Search in PATH environment variable
    path_in_env = search_in_path_env(app_name)
    if path_in_env:
        return path_in_env

    # Search in Start Menu
    path_in_start_menu = search_in_start_menu(app_name)
    if path_in_start_menu:
        return path_in_start_menu

    # Search in Windows Registry
    path_in_registry = search_in_registry(app_name)
    if path_in_registry:
        return path_in_registry

    # If not found, return None
    return None

def open_application(app_name):
    path = find_application_path(app_name)
    if path:
        try:
            subprocess.Popen([path])
            print(f"Opening {app_name}...")
        except Exception as e:
            print(f"Could not open {app_name}. Error: {e}")
    else:
        print(f"Application '{app_name}' not found on this system.")

def close_application(app_name):
    # Add .exe extension if not provided
    if not app_name.endswith(".exe"):
        app_name += ".exe"
    else:
        app_name=app_name

    # Use the Windows command `taskkill` to close the application
    try:
        os.system(f"taskkill /f /im {app_name}")
        print(f"Closed {app_name} if it was running.")
    except Exception as e:
        print(f"Could not close {app_name}. Error: {e}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("Ready to comply.What can i do for you?")

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if "matrix" in query:
            print("yes sir")
            speak("yes sir")

        elif 'what is' in query:
            speak('searching wikipedia....')
            query=query.replace("what is","")
            results= wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('searching wikipedia....')
            query=query.replace("who is","")
            results= wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open('google.com')
        
        elif'open google' in query:
            speak('what should i search for?')
            qry=takeCommand().lower()
            webbrowser.open(f'{qry}')
            results= wikipedia.summary(qry,sentences=2)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak('what would you like to watch?')
            qrry= takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif 'search on youtube' in query:
            query =query.replace('search on youtube',"")
            webbrowser.open(f'www.youtube.com/results?search_query={query}')

        elif 'close' in query:
            app_name = query.replace("close ", "").strip()
            close_application(app_name)

        elif 'type' in query:
            query=query.replace("type","")
            pyautogui.typewrite(f"{query}",0.1)

        elif 'open' in query:
            app_name = query.replace("open ", "").strip()
            open_application(app_name)