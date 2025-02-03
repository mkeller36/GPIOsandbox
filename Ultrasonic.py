from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=21, trigger=19)
while True:
    print(ultrasonic.distance)
