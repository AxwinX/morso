import os
import time
from console.utils import set_title

morse = {"a":"._","b":'-...',"c" : "_._.","d" : "_..","e" : ".","f" : ".._.","g" : "__.","h" : "....",
    "i" : "..","j" : ".___","k" : "_.-","l" : "._..","m" : "__","n" : "_.","o" : "___","p" : ".__.","q" : "__._",
    "r" : "._.","s" : "...","t" : "_","u" : ".._","v":"..._","w" : ".__","x" : "_.._","y" : "_.__","z":"__..",
    "1":".____","2":"..___","3":"...__","4":"...._","5":".....","6":"_....","7":"__...","8":"___..","9":"____.",
    "0":"_____","?":"..__..","!":"_._.__",".":"._._._",",":"__..__",";":"_._._.",":":"___...","+":"._._.","-":"_...._",
    "/":"_.._.","=":"_..._"}

clear = (lambda: os.system("cls"))

def title():
    print("""\t\t███▄ ▄███▓ ▒█████   ██▀███    ██████  ▒█████  
\t\t▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▒██    ▒ ▒██▒  ██▒
\t\t▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄   ▒██░  ██▒
\t\t▒██    ▒██ ▒██   ██░▒██▀▀█▄    ▒   ██▒▒██   ██░
\t\t▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒▒██████▒▒░ ████▓▒░
\t\t░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ 
\t\t░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░  ░ ▒ ▒░ 
\t\t░      ░   ░ ░ ░ ▒    ░░   ░ ░  ░  ░  ░ ░ ░ ▒  
\t\t       ░       ░ ░     ░           ░      ░ ░  \n\n\n""")

def text_morse():
    clear()
    title()
    set_title ("MorsO ─ Axwin | Text to Morse Code | ")
    print()
    print("[1] - Enter your text")
    print("[2] - Back")
    sel = input(">>")


    str1 = ""
    if sel == "1":
        text = input("Enter your text here >>").replace(" ","")
        for i in text:
            if i not in morse:
                print("The entered letter is not found in Morse Code Please enter a valid letter")
                time.sleep(2)
                home()
            str1 += morse[i] + " "
        print(f"The morse code is : {str1}\n\n")
        print("[1] - Go Back to Home page")
        print("[2] - Save Data")
        out = input(">>")
        if out == "1":
            print("Going Back in 3s")
            time.sleep(3)
            home()
        elif out == "2":
            with open("text_to_morse.txt", "a") as f:
                f.write(f"{str1}\n")
                print("Saved Successfully")
                f.close()
                time.sleep(2)
                home()
    elif sel == "2":
        home()
    else:
        print("Please select the options given")
        time.sleep(2)
        clear()
        text_morse()

def morse_text():
    clear()
    title()
    set_title ("MorsO ─ Axwin | Morse Code to Text | ")
    print()
    print("[1] - Enter Morse Code")
    print("[2] - Back")
    sel = input(">>")


    str1 = ""
    if sel == "1":
        text = input("Enter your morse code here >>")
        mor = text.split(" ")
        for i in mor:
            if i not in list(morse.values()):
                print("Entered Morse Code is not found enter a valid code")
                time.sleep(2)
                home()
            key = list(morse.keys())[list(morse.values()).index(i)]
            str1 += key   
        print(f"your text is : {str1}\n\n")
        print("[1] - Go Back to Home page")
        print("[2] - Save Data")
        out = input(">>")
        if out == "1":
            print("Going Back in 3s")
            time.sleep(3)
            home()
        elif out == "2":
            with open("morse_to_text.txt", "a") as f:
                f.write(f"{str1}\n")
                print("Saved Successfully")
                f.close()
                time.sleep(2)
                home()

    elif sel  == "2":
        home()
    else:
        print("Please select the options given")
        time.sleep(2)
        clear()
        morse_text()


def home():
    clear()
    set_title ("MorsO ─ Axwin | Morse Code Converter")
    title()
    print("[1] - Text to Morse Code")
    print("[2] - Morse Code to Text")
    print("[3] - Quit")
    sele = input(">>")

    if sele == "1":
        text_morse()
    elif sele == "2":
        morse_text()
    elif sele == "3":
        quit = (lambda: os.system("exit"))
        print("Closing in 3secs")
        time.sleep(3)
        quit()

home()
