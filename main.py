import os
import pyautogui
import time

exec(open("speech-sample.py").read())
exec(open("word-parsing.py").read())

# Small delay to let parsing to end
time.sleep(3)

# Read the final sentence from another file
with open("output.txt", 'r') as file:
    lines = file.readlines()
    if lines:
        final_sentence = lines[-1].strip()
        print(f'Command to be executed => "{final_sentence}"\n')
    else:
        final_sentence = ""

# Open a terminal and focus on it (you might need to adjust this command)
# Replace 'gnome-terminal' with your terminal emulator if necessary
# If you want to use the current terminal, keep it commented
# os.system('gnome-terminal')

# Delay to allow the terminal to open (if using an external terminal)
# time.sleep(2)

# Simulate typing the final sentence
if final_sentence:
    print("Typing command and executing ...")
    pyautogui.typewrite(final_sentence.lower(), interval=0.1)

    # Press Enter to execute the typed command
    pyautogui.press('enter')
else:
    print("No final sentence found in output.txt.")





