from gpiozero import Button 

button = Button(26)

button.wait_for_press()
print("the button has been pressed, as fortold in the prophecy")
