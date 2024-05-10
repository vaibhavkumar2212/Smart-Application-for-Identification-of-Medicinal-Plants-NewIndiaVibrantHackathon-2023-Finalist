import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
