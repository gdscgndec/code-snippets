import pyttsx3
speaker = pyttsx3.init()
s=input(str('enter text'))
speaker.say(s)
speaker.runAndWait()
