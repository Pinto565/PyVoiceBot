import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('waiting for your command...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', ',')
                print(command)
    except:
        pass
    return command


def run_siri():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%x')
        speak('Todays date is ' + date)
    elif 'are you single' in command:
        speak('I am in a relationship')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    else:
        speak('Please repeat the command.')


while True:
    run_siri()