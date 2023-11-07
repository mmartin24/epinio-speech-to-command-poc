
# Python program to translate
# speech to text 
# Tweaked from: https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

import speech_recognition as sr

# Initialize the speech recognizer
r = sr.Recognizer()

# Define a function to convert speech to text
def record_text():
    # Continuously listen for and convert speech to text
    while True:
        try:
            # Use the microphone as the input source
            with sr.Microphone() as source:
                # Adjust for ambient noise to improve recognition
                r.adjust_for_ambient_noise(source, duration=0.2)
                # Listen for the user's input
                audio2 = r.listen(source)
                # Use Google's speech recognition service to convert audio to text
                MyText = r.recognize_google(audio2)
                # Convert the recognized text to lowercase
                MyText = MyText.lower()
                return MyText
        except sr.RequestError as e:
            # Handle the case where the recognition request fails
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            # Handle the case where the input speech is not recognized
            print("An unknown error occurred")

# Define a function to write the recognized text to an output file
def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()

# Uncomment the following lines if you want to continuously record and output text
# while True:
text = record_text()
output_text(text)