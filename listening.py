
from gpiozero import LED, Button
from threading import Thread 
from signal import pause
import signal
import sys
import requests
import sounddevice as sd
import scipy.io.wavfile as wav

import teddy_bear_rasp 

teddy_rasp = teddy_bear_rasp.TeddyBearRasp()

BUTTON_LISTEN_PIN = 18
LED_SEND = 27

button_listen = Button(BUTTON_LISTEN_PIN)
led_send = LED(LED_SEND)



def sending():
	"""Function to blink an LED during the recording duration."""
	led_send.blink(on_time=0.5, off_time=0.5, n=None, background=False)

def listen_and_send():
	led_thread = Thread(target=sending)
	led_thread.start()
	
	teddy_rasp.listen()
	
	led_send.off()
	led_thread.join()

def end():
	print("Cleaning up...")
	button_listen.close()
	led_send.close()

def signal_handler(sig, frame):
    print('Signal received, ending the program.')
    end()
    sys.exit(0)	

if __name__ == "__main__":

	try:
		signal.signal(signal.SIGINT, signal_handler)

		button_listen.when_pressed = listen_and_send
		print("Waiting for button press..")
		pause()
		
	
	except Exception as e:
		print(f"An error occurred: {e}")
		
	finally:
		end()
