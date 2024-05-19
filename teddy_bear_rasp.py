
import asyncio
import io
import pygame
import scipy.io.wavfile as wav
import sounddevice as sd
import requests

# from gpiozero import LED, Button
from fastapi import FastAPI, File, UploadFile, Request
from threading import Thread 

FORMAT = 'int16'
CHANNELS = 1
RATE = 44100
CHUNK = 1#1024
RECORD_SECONDS = 5
OUTPUT_FILENAME="output.wav"


RECEIVE_URL = "http://localhost:8000/speak"
SEND_URL = "http://localhost:8000/listen"



# TeddyBearRasp Class
class TeddyBearRasp: 

    def send_audio_file(self, filename, url):
        
        with open(filename, 'rb') as f:
            files = {'audio': f}
            response = requests.post(url, files=files)
            print("Send complete!")
        


    def listen(self):

        # Start recording
        recording = sd.rec(
            int(RECORD_SECONDS * RATE), 
            samplerate=RATE,
            channels=CHANNELS,
            dtype=FORMAT
            )
        sd.wait()

   
        wav.write(OUTPUT_FILENAME, RATE, recording)
        
        self.send_audio_file(OUTPUT_FILENAME, SEND_URL)


    async def speak(self, audio: UploadFile = File(...)):
        audio_content = await audio.read()	
        pygame.mixer.init()
        
        audio_stream = io.BytesIO(audio_content)
        
        pygame.mixer.music.load(audio_stream, "wav")
        pygame.mixer.music.play()



        
