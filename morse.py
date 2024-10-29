import tkinter as tk
import time
import threading
import platform

if platform.system() == 'Windows':
    import winsound
else:
    from playsound import playsound

MORSE_CODE_DICT ={
'!':"-.-.--",
'"':".-..-.",
'$':"...-..-",
'&':".-...",
"'":".----.",
'(':"-.--.",
')':"-.--.-",
'+':".-.-.",
',':"--..--",
'-':"-....-",
'.':".-.-.-",
'/':"-..-.",
'0':"-----",
'1':".----",
'2':"..---",
'3':"...--",
'4':"....-",
'5':".....",
'6':"-....",
'7':"--...",
'8':"---..",
'9':"----.",
':':"---...",
';':"-.-.-.",
'=':"-...-",
'?':"..--..",
'@':".--.-.",
'_':"..--.-",
'A':".-",
'B':"-...",
'C':"-.-.",
'D':"-..",
'E':".",
'F':"..-.",
'G':"--.",
'H':"....",
'I':"..",
'J':".---",
'K':"-.-",
'L':".-..",
'M':"--",
'N':"-.",
'O':"---",
'P':".--.",
'Q':"--.-",
'R':".-.",
'S':"...",
'T':"-",
'U':"..-",
'V':"...-",
'W':".--",
'X':"-..-",
'Y':"-.--",
'Z':"--.."
}

DOT_DURATION = 0.1 
DASH_DURATION = 0.3  
FREQUENCY = 700 

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text.upper() if char in MORSE_CODE_DICT)


def play_morse_code(morse_code):
    for char in morse_code:
        if char == '.':
            if platform.system() == 'Windows':
                winsound.Beep(FREQUENCY, int(DOT_DURATION * 1000))
            else:
                playsound("dot.wav") 
            time.sleep(DOT_DURATION)
        elif char == '-':
            if platform.system() == 'Windows':
                winsound.Beep(FREQUENCY, int(DASH_DURATION * 1000))
            else:
                playsound("dash.wav") 
            time.sleep(DASH_DURATION)
        else:
            time.sleep(DOT_DURATION) 
def play_in_thread(morse_code):
    thread = threading.Thread(target=play_morse_code, args=(morse_code,))
    thread.start()

def setup_gui():
    def convert_and_play():
        input_text = text_entry.get()
        morse_code = text_to_morse(input_text)
        morse_label.config(text=f"Morse Code: {morse_code}")
        play_in_thread(morse_code)

    root = tk.Tk()
    root.title("Morse Code Translator")

    tk.Label(root, text="Enter Text:").pack()
    text_entry = tk.Entry(root, width=50)
    text_entry.pack()

    convert_button = tk.Button(root, text="Convert & Play", command=convert_and_play)
    convert_button.pack()

    morse_label = tk.Label(root, text="Morse Code:")
    morse_label.pack()

    root.mainloop()


setup_gui()
