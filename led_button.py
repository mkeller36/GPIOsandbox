from gpiozero import LED, Button

import subprocess

button = Button(26)


button.wait_for_press()

print("congratulations")

subprocess.run(["python","led_blink.py"])

