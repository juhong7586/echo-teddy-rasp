import asyncio
import pyaudio
import pygame
import time
import subprocess

from gpiozero import LED, Button
from pydub import AudioSegment 
from io import BytesIO
from signal import pause
from time import sleep 

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10 
OUTPUT_FILENAME="output.mp3"

led_send = LED(27)
led_receive = LED(22)
button_power = Button(24)
button_listen = Button(17)
audio = pyaudio.PyAudio()


def run_script():
    print("Power Button pressed. Running app.py...")
    subprocess.run(['python3', 'app.py'])



def listen():
    if button_listen.is_pressed:
        # start streaming 
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("Recording...")

        raw_buffer = BytesIO()

        for _ in range(0,int(RATE / CHUNK)):
            data = stream.read(CHUNK)
            raw_buffer.write(data)

        print("Finished recording.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        raw_buffer.seek(0)
        
        # make file 
        audio_segment = AudioSegment.from_raw(raw_buffer, sample_width=2, frame_rate=RATE, channels=CHANNELS)
        
        mp3_buffer = BytesIO()
        audio_segment.export(OUTPUT_FILENAME, format="mp3")

        mp3_buffer.seek(0)

        with open("output.mp3", "wb") as f:
            f.write(mp3_buffer.read())
        print("Saved MP3 file to output.mp3")


def speak(path):
    led_receive.off()
    
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

def sending():
    led_receive.off()
    
    while True: 
        led_send.on()
        asyncio.sleep(0.1)
        led_send.off()
        asyncio.sleep(0.1)


def receiving():
    led_send.off()

    while True: 
        led_receive.on()
        asyncio.sleep(0.1)
        led_receive.off()
        asyncio.sleep(0.1)

    
# button_power.when_pressed = run_script 
# print("System ready. Press the button to run the script.")

# pause()


if __name__ == "__main__":
    listen()