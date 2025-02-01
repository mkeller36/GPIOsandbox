from gpiozero import LightSensor, Buzzer

ldr = LightSensor(21)

while True: 
    print(ldr.value)
