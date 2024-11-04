import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None
def execute_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif 'open website' in command:
        speak("Which website do you want to open?")
        website = listen()
        if website:
            url = f"http://{website.strip()}.com"
            webbrowser.open(url)
            speak(f"Opening {website.strip()}")

    elif 'play music' in command:
        music_dir = "path_to_your_music_directory"  
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))  
        speak("Playing music.")

    elif 'stop' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I am sorry, I cannot help with that.")
if _name_ == "_main_":
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        if command:
            execute_command(command)
