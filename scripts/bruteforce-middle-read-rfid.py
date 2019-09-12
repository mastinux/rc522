#!/usr/bin/env python3

# https://github.com/pimylifeup/MFRC522-python/blob/master/mfrc522/SimpleMFRC522.py

#!/usr/bin/env python3

from time import sleep
import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def custom_read():
        print("Trying key = %s" % key)

        ret = 0

        try:
                id, text = reader.read()

                if text != "":
                        os.system("echo %s >> keys.txt" % reader.KEY)
                else:
                        ret = 1

        finally:
                GPIO.cleanup()

        os.system("echo %s > last_key.txt" % key)
        sleep(.333)

        return ret


def brute_force_key(key, start_key, step, max_steps):
	if step == max_steps:
		reader.KEY = key
		return custom_read()

	start = 0

	if start_key[step] != -1:
		start = start_key[step]
		start_key[step] = -1

	for i in range(start, 256):
		key[step] = i

		stop = brute_force_key(key, start_key, step + 1, max_steps)

		if stop == 0:
			me = os.getpid()
			p = psutil.Process(me)
			p.kill()


step = 0
#reader = SimpleMFRC522()
start_key = [255,255,255,254,0,0]
key = [0,0,0,0,0,0]
brute_force_key(key, start_key, step, 6)

