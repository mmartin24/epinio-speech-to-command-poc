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
- Fine tune the speech recognition as much as possible.
- Transcribe the speech to text
- Execute a successful transcription into a functional command 

If all the above works somehow next step would be to attempt a more human-friendly interpretation of a command. For instance, instead of transcribing `epinio app create sampleapp `, it would be nice that a sentence like: "Epinio, please create an app named sampleapp", would execute that command producing the same result.

## Resources

Not sure where I will end, but I am starting here:
https://geekscoders.com/python-speech-recognition-tutorial-for-beginners/
https://people.csail.mit.edu/hubert/pyaudio/#downloads

## Demo results
Note: you may want to enable / turn on volume on both videos to see the result

#### Demo 1: Transcription of Epinio commands

https://github.com/mmartin24/epinio-speech-to-command-poc/assets/37271841/28812e41-a55f-4509-b99d-064cccbc3a80


#### Demo 2: Complex Epinio command transformation from "human-friendly" speech: 

https://github.com/mmartin24/epinio-speech-to-command-poc/assets/37271841/ca012de9-9861-444f-bc56-7f831ea325e7
