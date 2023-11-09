# Epinio speech-to-command POC

## Project Description
This project is born thanks to [SUSE Hack Week](https://hackweek.opensuse.org/) 23, where employees at this nice company are given a week time to learn, develop, and grow.

My goal here is to attempt to build a basic speech-to-text app that can execute some basic CLI commands for [Epinio](https://epinio.io/) simply using voice without touching a keyboard. Examples:

```
epinio app create sampleapp
epinio app list
```

I believe that this could be useful not only to ease command typing at times but perhaps be also a nice feature that could add value to Epinio if successful.

## Goal for this Hackweek
Some of the goals for this project would be:

- Find some tools that already bring a speech-to-text library
- Put together a basic script that somehow works and can recognize voice.
- Fine-tune the speech recognition as much as possible.
- Transcribe the speech to text
- Execute a successful transcription into a functional command 

If all the above works somehow next step would be to attempt a more human-friendly interpretation of a command. For instance, instead of transcribing `epinio app create sampleapp `, it would be nice that a sentence like: "Epinio, please create an app named sampleapp", would execute that command producing the same result.


## Demo results
Note: you may want to enable/turn on volume on both videos to see the result

#### Demo 1: Transcription of Epinio commands

https://github.com/mmartin24/epinio-speech-to-command-poc/assets/37271841/28812e41-a55f-4509-b99d-064cccbc3a80


#### Demo 2: Complex Epinio command transformation from "human-friendly" speech: 

https://github.com/mmartin24/epinio-speech-to-command-poc/assets/37271841/ca012de9-9861-444f-bc56-7f831ea325e7

## Requirements

Note: for the time being current instructions are centered in Linux users. To be expanded.


Main installs:
- Install [Epinio](https://epinio.io/). If you are unsure about how to install visit: https://docs.epinio.io/installation/install_epinio
- [Python](https://www.python.org/downloads/) (Preferably > 3.10.0). If not installed, download it here: https://www.python.org/downloads/
- [PIP](https://pypi.org/project/pip/) to install the required packages. If not installed check here: https://pip.pypa.io/en/stable/installation/

    For Linux users, you can use:
    ```
    wget https://bootstrap.pypa.io/get-pip.py
    python3 ./get-pip.py
    ```

- Other installs:

    **Python Speech Recognition module**: 
    ```
    pip3 install speechrecognition
    ```
    **PyAudio**:
    ```
    pip install pyaudio
    ```
    Alternatively Ubuntu 22.04 users may install it with:
    ```
    sudo apt-get install python3-pyaudio
    ```

    **PyAutoGUI**
    ```
    pip3 install PyAutoGUI
    ```

    **tkinter** (If not installed already)
    ```
    sudo apt-get install python3-tk python3-dev
    ```

## How to run it

Run on terminal:
```python
python3 main.py
```

Alternatively you may want to run it as this if an errors related to ALSA like [this](https://github.com/Uberi/speech_recognition#on-ubuntudebian-i-get-annoying-output-in-the-terminal-saying-things-like-bt_audio_service_open--connection-refused-and-various-others) appears :

```python
 python3 main.py 2>/dev/null
```

After this, you will see the following text in your terminal prompting you to say a command:
`Please say the Epinio command you wish to be executed`

Speak as clear as possible so the program has better chance to recognize the words.
Later, the program will try to interpret your speech, parse the words and transform it into a working command.

## Resources used

https://geekscoders.com/python-speech-recognition-tutorial-for-beginners/
https://people.csail.mit.edu/hubert/pyaudio/#downloads
https://github.com/Uberi/speech_recognition
