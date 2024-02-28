import win32com.client as win
speaker = win.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter what you want to say: ")
    s = input()
    if s == 'q':
        b = "Bye Bye friends"
        speaker.Speak(b)
        break
    speaker.Speak(s)

# To stop the program press
# q
