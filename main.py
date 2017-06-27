# pylint: skip-file
# Requires PyAudio and PySpeech.

import speech_recognition

lang = 'he-il'
recognizer = speech_recognition.Recognizer()

def record():
    with speech_recognition.Microphone() as source:
        print("Say something!")
        return recognizer.listen(source)

try:
    audio = record()
    print("You said: " + recognizer.recognize_google(audio, language=lang)) # key="GOOGLE_SPEECH_RECOGNITION_API_KEY
except speech_recognition.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except speech_recognition.RequestError as err:
    print("Could not request results from Google Speech Recognition service; {0}".format(err))