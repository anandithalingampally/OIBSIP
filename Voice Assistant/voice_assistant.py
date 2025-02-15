import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Captures and processes voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Couldn't understand. Please try again.")
            return None
        except sr.RequestError:
            print("API request error. Check your internet connection.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def execute_command(command):
    """Executes actions based on recognized voice commands."""
    if not command:
        return

    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching Google for {search_query}")
        else:
            speak("Please specify what to search for.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Voice assistant activated. Say 'exit' to stop.")
    while True:
        user_command = recognize_speech()
        execute_command(user_command)
