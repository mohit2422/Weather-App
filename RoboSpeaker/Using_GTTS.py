import gtts
import playsound

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 0.1. Created by Mohit")
    text = input("Enter what you want to say: ")
    sound = gtts.gTTS(text, lang="en")
    sound.save("welcome.mp3")
    playsound.playsound("welcome.mp3")

