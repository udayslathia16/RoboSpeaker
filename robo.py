import os
import win32com.client
if __name__=='__main__':
    while True:

        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        x=input("Enter what you want to say :")
        if x=="q":
            speaker.speak("bye bye friends")
            break
        
        speaker.speak(x)